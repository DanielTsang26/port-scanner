
**PortHound** is a lightweight Python-based network reconnaissance tool for scanning host availability, scanning ports, and OS detection. It provides a CLI interface with rich output and optional summary views using the `rich` library.


---

## Features
- History Logging (CSV format): OPEN | CLOSE | TIMESTAMP
- Sample OS Detection
- Host Discovery
- Port Scanning
- Detailed & Overview Nmap visualization through RICH library table views.
- CLI flags for history view, summary display, and port scan options

## Usage
 ### Menu:
![image](https://github.com/user-attachments/assets/681fa634-f30f-4128-bcda-680f027d90dd)

## Example of Usage
``
python main.py --target 8.8.8.8 --ports 25-30 --host-discovery --detailed 
``
### Output:

![image](https://github.com/user-attachments/assets/e87f8c35-39bf-4c47-a175-9508a15968a0)

## Diagram on how a Port Scanner works:
![image](https://github.com/user-attachments/assets/f67e75f6-6d38-4921-a260-634855e95f30)


## Requirements:
- Python 3.8+
- Rich
  
