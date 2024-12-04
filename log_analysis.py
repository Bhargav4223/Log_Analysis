import re
import csv
from collections import defaultdict

# File names
LOG_FILE = "sample.log"
OUTPUT_FILE = "log_analysis_results.csv"
FAILED_LOGIN_THRESHOLD = 10

def parse_logs(file_path):
    """Reads the log file and extracts required data."""
    ip_counts = defaultdict(int)
    endpoint_counts = defaultdict(int)
    failed_login_attempts = defaultdict(int)
    # Regex patterns for the recognization of the patterns 
    ip_pattern = r"^(\d+\.\d+\.\d+\.\d+)"
    endpoint_pattern = r"\"(?:GET|POST) (\S+)"
    failed_login_pattern = r" 401 |Invalid credentials"

    with open(file_path, "r") as file:
        for line in file:
            # Extract IP address
            ip_match = re.search(ip_pattern, line)
            if ip_match:
                ip = ip_match.group(1)
                ip_counts[ip] += 1

            # Extract endpoint
            endpoint_match = re.search(endpoint_pattern, line)
            if endpoint_match:
                endpoint = endpoint_match.group(1)
                endpoint_counts[endpoint] += 1

            # Check for failed login attempts
            if re.search(failed_login_pattern, line):
                if ip_match:
                    failed_login_attempts[ip] += 1

    return ip_counts, endpoint_counts, failed_login_attempts

def write_to_csv(ip_counts, most_accessed_endpoint, failed_login_attempts, output_file):
    """Writes the results to a CSV file."""
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write IP Request Counts
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
            writer.writerow([ip, count])

        # Write Most Accessed Endpoint
        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint", "Access Count"])
        writer.writerow([most_accessed_endpoint[0], most_accessed_endpoint[1]])

        # Write Suspicious Activity
        writer.writerow([])
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in failed_login_attempts.items():
            if count > FAILED_LOGIN_THRESHOLD:
                writer.writerow([ip, count])

def main():
    # Parse the logs
    ip_counts, endpoint_counts, failed_login_attempts = parse_logs(LOG_FILE)

    # Identify the most accessed endpoint
    most_accessed_endpoint = max(endpoint_counts.items(), key=lambda x: x[1])

    # Display the results
    print("IP Address Request Counts:")
    for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip:<20} {count}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")

    print("\nSuspicious Activity Detected:")
    suspicious_detected = False
    print(f"{'IP Address':<20} {'Failed Login Attempts'}")
    for ip, count in failed_login_attempts.items():
        if count > FAILED_LOGIN_THRESHOLD:
            print(f"{ip:<20} {count}")
            suspicious_detected = True
    # Display the else case if there is no exceeding of the threshold.
    if not suspicious_detected:
        print("No IP addresses exceeded the failed login threshold.")

    # Write results to CSV
    write_to_csv(ip_counts, most_accessed_endpoint, failed_login_attempts, OUTPUT_FILE)
    print(f"\nResults saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
