# Ghostshell

### A Terminal-Based Lab Environment Manager for Cybersecurity Research

Ghostshell is a TUI (Textual User Interface) application designed to orchestrate containerized vulnerability labs. It provides a clean, efficient interface for defining, running, and managing security test cases, helping researchers and students study vulnerabilities in a controlled and repeatable way.

*Note: You would replace the URL below with a real screenshot of your application.*
![Ghostshell TUI Screenshot](https://user-images.githubusercontent.com/your-username/your-repo/assets/ghostshell_screenshot.png)

## About The Project

In cybersecurity research, setting up a specific environment to test a vulnerability can be repetitive and time-consuming. Ghostshell automates this entire workflow. By defining your lab environments in simple YAML profile files, you can launch a complete test case with a single keystroke.

## Features

* **Terminal-Native UI:** A modern and responsive interface built with Textual.
* **Profile-Based Labs:** Define complex test environments using simple YAML files.
* **Docker Integration:** Automatically pulls Docker images, and starts and stops containers for each lab.
* **Automated PoC Execution:** Runs associated proof-of-concept scripts against the target environment.

## Getting Started

### Prerequisites

* Python 3.8+
* Docker must be installed and running on your system.

### Installation

1.	 **Clone the repository:**
    ```sh
    Git clone [https://github.com/your-username/ghostshell.git](https://github.com/your-username/ghostshell.git)
    Cd ghostshell
    ```

2.	 **Create and activate a Python virtual environment:**
    ```sh
    # On macOS & Linux
    Python3 -m venv venv
    Source venv/bin/activate

    # On Windows
    Python -m venv venv
    .\venv\Scripts\activate
    ```

3.	 **Install the required packages:**
    ```sh
    Pip install -r requirements.txt
    ```

## Usage

Launch the application by running the main Python script:

```sh
Python ghostshell/profile_manager.py
