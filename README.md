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

### 🎯 What This Tool Does (Step-by-Step)

1. **Connect to AWS** using the `boto3` Python SDK with your IAM credentials.
2. **Fetch all EC2 Security Groups** in your account.
3. For each Security Group:
   - Look at **inbound rules**.
   - Check if any sensitive ports (22, 3389, 3306, etc.) are open to **`0.0.0.0/0`**.
4. **Flag each insecure rule** with details:
   - Port number
   - Protocol
   - Security Group name and ID
   - Risk level
5. Output the results in:
   - Console (basic view)
   - Optional: Save as CSV or JSON report
   - Optional: Send email or Slack alert
6. (Optional Phase 2): **Auto-remediate** insecure rules if configured (e.g., remove rule or restrict it to your IP).

---

### 🧰 Tools & Technologies Used

| Tool / Library | Purpose |
|----------------|---------|
| **Python** | Scripting and automation |
| **boto3** | AWS SDK for Python |
| **AWS IAM User** | Authenticated access to EC2 Security Groups |
| **AWS EC2** | For fetching Security Groups |
| **Security Group rules** | To find exposed ports |
| *(Optional)* Pandas | For creating reports |
| *(Optional)* smtplib / Slack Webhook | To send alerts |

---

### 🔍 What Ports Are Considered Risky?
You can customize this list, but common ones include:
- `22` (SSH)
- `3389` (RDP)
- `3306` (MySQL)
- `5432` (PostgreSQL)
- `6379` (Redis)
- `9200` (Elasticsearch)
- Any port not meant for public access

---

### ✅ What You'll Learn

- Auditing AWS network configurations
- Using AWS SDKs securely (boto3, IAM roles)
- Identifying misconfigurations
- Following **cloud security best practices**
- Writing clean, extensible Python scripts
- Automating routine security checks (like DevSecOps pros do)

---

### 🌱 Future Enhancements

- Add support for **multiple cloud providers** (Azure, GCP).
- Visualize results in a dashboard (e.g., using Streamlit or Flask).
- Integrate with **SIEM tools** like Splunk or Elastic.
- Schedule this script as a **Lambda function or CRON job**.
- Send automatic Slack/email/Teams alerts.

---
