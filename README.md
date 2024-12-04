# Log Analysis Script

## 📄 Description

This repository contains a Python script designed to analyze server log files. The script provides valuable insights into server activity by extracting and analyzing key information, including request counts, frequently accessed endpoints, and potential suspicious activity such as brute force login attempts. It is optimized for scalability, making it suitable for large log datasets.

---

## ✨ Features

1. **Count Requests per IP Address**  
   - Parses the log file to count the number of requests made by each IP address.  
   - Results are sorted in descending order of request counts.  
   - Example output:
     ```plaintext
     IP Address           Request Count
     192.168.1.1          234
     203.0.113.5          187
     10.0.0.2             92
     ```

2. **Identify the Most Frequently Accessed Endpoint**  
   - Extracts and identifies the endpoint (e.g., URL) accessed the highest number of times.  
   - Example output:
     ```plaintext
     Most Frequently Accessed Endpoint:
     /home (Accessed 403 times)
     ```

3. **Detect Suspicious Activity**  
   - Flags potential brute force login attempts based on failed login entries (e.g., HTTP status code `401` or failure messages).  
   - Identifies IP addresses exceeding a configurable threshold for failed login attempts (default: 10).  
   - Example output:
     ```plaintext
     Suspicious Activity Detected:
     IP Address           Failed Login Attempts
     192.168.1.100        56
     203.0.113.34         12
     ```

4. **Save Results to CSV**  
   - Outputs analysis results into a CSV file named `log_analysis_results.csv`.  
   - The CSV file includes:  
     - **Requests per IP**: Columns: `IP Address`, `Request Count`  
     - **Most Accessed Endpoint**: Columns: `Endpoint`, `Access Count`  
     - **Suspicious Activity**: Columns: `IP Address`, `Failed Login Count`  

---

## 🛠️ Installation & Usage

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/log-analysis-script.git
   cd log-analysis-script
   ```

2. **Install Dependencies**  
   The script uses Python 3 and requires no external libraries. Ensure Python 3 is installed on your system.

3. **Run the Script**  
   Save your log file as `sample.log` or modify the script to specify your log file name. Run the script using:  
   ```bash
   python log_analysis.py
   ```

4. **View Results**  
   - The results are displayed in the terminal.
   - A CSV file named `log_analysis_results.csv` is created in the working directory.

---

## 📝 Configuration

- **Failed Login Threshold**  
  You can modify the threshold for flagging suspicious activity by changing the `FAILED_LOGIN_THRESHOLD` variable in the script.  
  ```python
  FAILED_LOGIN_THRESHOLD = 10
  ```

---

## 🧪 Example Input & Output

### Sample Log File (`sample.log`)
```plaintext
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
...
```

### Output Example
#### Terminal Output:
```plaintext
IP Address Request Counts:
203.0.113.5          8
198.51.100.23        8
192.168.1.1          7
10.0.0.2             6
192.168.1.100        5

Most Frequently Accessed Endpoint:
/login (Accessed 13 times)

Suspicious Activity Detected:
IP Address           Failed Login Attempts
203.0.113.5          8
192.168.1.100        5

Results saved to log_analysis_results.csv
```

#### CSV File (`log_analysis_results.csv`):
| IP Address       | Request Count |  
|------------------|---------------|  
| 203.0.113.5      | 8             |  
| 198.51.100.23    | 8             |  

| Endpoint | Access Count |  
|----------|--------------|  
| /login   | 13           |  

| IP Address       | Failed Login Count |  
|------------------|--------------------|  
| 203.0.113.5      | 8                  |  
| 192.168.1.100    | 5                  |  

---

## 🧩 Future Improvements

- Add support for additional log formats.  
- Implement visualization for the analysis results.  
- Include support for multi-threading to handle very large files efficiently.  

---
