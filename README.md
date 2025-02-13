# File Hash Generator

[![Made With Love](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F-by%20Jonathan-red)](https://github.com/MrGuato/File-Hash-Generator)
[![Downloads](https://img.shields.io/github/downloads/MrGuato/File-Hash-Generator/total)](https://github.com/MrGuato/File-Hash-Generator/releases)
[![Stars](https://img.shields.io/github/stars/MrGuato/File-Hash-Generator)](https://github.com/MrGuato/File-Hash-Generator/stargazers)
![Forks](https://img.shields.io/github/forks/MrGuato/File-Hash-Generator)
![Issues](https://img.shields.io/github/issues/MrGuato/File-Hash-Generator)
![Last Commit](https://img.shields.io/github/last-commit/MrGuato/File-Hash-Generator)
![Top Language](https://img.shields.io/github/languages/top/MrGuato/File-Hash-Generator)
![License](https://img.shields.io/github/license/MrGuato/File-Hash-Generator)

**Description:** This program efficiently generates the SHA-256, SHA-1, or MD5 hash of files. This is particularly useful for cybersecurity professionals who need to quickly verify the integrity and authenticity of potentially malicious files, especially when dealing with large files that exceed upload limits on online analysis platforms.

**Problem Statement:**  Many free online malware analysis sites, such as Hybrid Analysis and Joe Sandbox, impose file size limits (e.g., 100MB).  This makes it difficult to analyze large executables directly.  This program solves this problem by enabling users to quickly generate a file's hash, which can then be submitted to these services for analysis instead of the entire file. This significantly speeds up the analysis process and bypasses file size restrictions.

**Solution:** Our File Hash Generator program addresses this issue by employing a robust and efficient algorithm that can handle large files without errors or performance degradation. The program generates the SHA-256, SHA-1, or MD5 hash of the input file, which is a widely accepted and reliable method for file authentication.  This allows users to analyze large files indirectly by submitting their hashes to online services.

**Use Cases:**

* Cybersecurity professionals can use this program to generate hashes for suspicious files, especially those exceeding upload limits on free online analysis platforms.
* The generated hash can be submitted to various malware analysis tools, such as:
    * VirusTotal (virustotal.com)
    * JoeSandbox (joesandbox.org)
    * Hybrid Analysis (hybrid-analysis.com)
* The hash can also be used for local file integrity monitoring and verification purposes.

**How to Use:**

1. Run the program.
2. Select the file you wish to generate a hash for.
3. Choose the desired hashing algorithm (SHA-256, SHA-1, or MD5).
4. Wait for the program to complete its calculation.
5. The generated hash will be displayed in the output window.
6. Copy the hash, and happy hunting! 

**Example Usage:** Suppose you have a 501MB executable file that you suspect may contain malware.  You can use our program to generate its SHA-256 hash. You then submit this hash to VirusTotal or JoeSandbox for analysis. If multiple tools detect malicious activity associated with this specific hash, it’s highly likely that the file is indeed malicious.  This process avoids the need to upload the entire 500MB file.

**Hashes for Verification:**

- **MD5:** 101c7af487aa899fa66791d66ba26c5e
- **SHA-1:** d4d0e581aa67901d7128a6dbfc72e9547cd663f2
- **SHA-256:** 633fc41cd08fc7b8584e48cd90b427943a03c95c77fbebe6a22f5e6ba8c20c65

**Future Development:** Plan to enhance this program by:

* Adding support for other hashing algorithms (e.g., BLAKE2, SHA-3).
* Improving the user interface and experience.
* Exploring integration with virustotal to search for the hash
* Dark Mode
* See about Signing the Program with a CA
