# 🔐 Cloud Port Exposure Auditor  
## *(aka: "Find My Open Ports")*

---

### 📌 **Project Summary**

This project is a **Python-based cloud security auditing tool** that analyzes your AWS EC2 **Security Groups** to detect **exposed ports** — specifically, those open to the **entire internet (`0.0.0.0/0`)**.

Its goal is to help identify **risky misconfigurations** where sensitive ports like **SSH (22)** or **RDP (3389)** are publicly accessible, which can leave your cloud infrastructure vulnerable to brute-force attacks, malware injections, and unauthorized access.

This tool simulates part of what a **Cloud Security Engineer (Blue Team)** does during a **routine audit** to ensure the **principle of least privilege** is enforced across the network.

---

### 🧠 Why This Matters

Cloud services are flexible but also prone to misconfiguration. One of the most **common cloud security risks** is unintentionally exposing sensitive services (like SSH or RDP) to the public.

> Many real-world breaches have occurred because a developer left `22` or `3306` open to the world.

This project teaches you how to:
- Think like a security engineer
- Work with **Infrastructure-as-Code principles**
- Use **AWS SDKs and security best practices**
- Build automation tools for **real-world compliance & auditing**

---

### 🌟 What This Tool Does (Step-by-Step)

1. **Connect to AWS** using the `boto3` Python SDK with your IAM credentials.
2. **Fetch all EC2 Security Groups** in your account (across all AWS regions).
3. For each Security Group:
   - Look at **inbound rules**.
   - Check if any sensitive ports (22, 3389, 3306, etc.) are open to **`0.0.0.0/0`** or **`::/0`**.
4. **Flag each insecure rule** with details:
   - Port number
   - Protocol
   - Security Group name and ID
   - Risk level
5. Output the results in:
   - Console (basic view)
   - Optional: Save as CSV or JSON report
   - Optional: Send email or Slack alert
6. *(Optional Phase 2)*: **Auto-remediate** insecure rules if configured (e.g., remove rule or restrict it to your IP).

---

### 🧰 AWS Configuration (Step-by-Step)

1. **Login to AWS Console**
2. Navigate to **IAM > Users > Add User**
   - Name: `cloud-auditor`
   - Access type: `Programmatic access`
3. Assign the user the **AmazonEC2ReadOnlyAccess** policy *(or a custom one with `ec2:DescribeSecurityGroups`)*
4. Download the access key & secret key (used in boto3 or `aws configure`)

---

### 🔧 Local Environment Setup

1. **Install AWS CLI**:
   ```bash
   brew install awscli  # or sudo apt install awscli
   aws configure  # Enter access key, secret, region, and json as output
   ```

2. **Install Python dependencies**:
   ```bash
   pip install boto3 pandas requests
   ```

3. (Optional) **Activate a virtual environment**:
   ```bash
   python -m venv venv && source venv/bin/activate
   ```

---

### 🚀 How to Run the Tool

```bash
python auditor.py
```

This will:
- Loop through all AWS regions
- Scan every EC2 security group
- Detect risky ports open to the internet
- Output results to the console and `exposed_ports_<timestamp>.csv/json`

---

### 📊 Sample Output
```
🌐 Scanning region: us-east-1
🔥 ssh-group (sg-xxxx) exposes port 22/tcp to 0.0.0.0/0
🔥 db-group (sg-yyyy) exposes port 3306/tcp to ::/0
```

---

### 📄 Output Files
- `exposed_ports_YYYYMMDD_HHMMSS.csv`
- `exposed_ports_YYYYMMDD_HHMMSS.json`

---

### 🔍 Ports Considered Risky (Customizable)
- `22` (SSH)
- `3389` (RDP)
- `3306` (MySQL)
- `5432` (PostgreSQL)
- `6379` (Redis)
- `9200` (Elasticsearch)

> Edit the `RISKY_PORTS` list in the script to change these.

---

### 📚 Future Plans (Optional Phase 2)
- [ ] Slack alerting via webhook
- [ ] Email alerting via SMTP or AWS SES
- [ ] Auto-remediation for public rules
- [ ] Flask dashboard for visualization
- [ ] Multi-account/org-wide auditing with STS

---

### 🏦 Project Folder Structure
```
cloud-port-auditor/
├── auditor.py                # Single-region version
├── multi_region_auditor.py  # Multi-region scanner + export
├── exposed_ports_*.csv      # Output report
├── requirements.txt
└── README.md
```

---

### 🏠 Author
Built with ❤️ by Sharath Chandra Mummadi

---

### 🔒 Security Note
This tool is meant for **auditing and educational purposes**. Do not leave publicly exposed ports unless strictly required.

> Security is not a one-time action. It is a continuous process.

