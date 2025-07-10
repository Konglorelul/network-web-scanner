# Security tool for networks and web applications
Developed a security scanning tool in Python as part of my diploma project, capable of detecting vulnerabilities in network infrastructures and web application with specific modules for each task. The platform includes modules for host discovery, port scanning, known vulnerabilities identification and SQLi/XSS reflected vulnerabilities. All the results can be saved in .xls files for further analysis.

The script nw.py is the entry point for the whole platform, the rest of the scripts are modules for each function. 
The script porthost_scanner has most of the networking scanning functionalities + vuln_scanner is using the VULNERS API for data search in their database.
The final two scripts find specific XSS and SQLi vulnerabilities on the DVWA application.
