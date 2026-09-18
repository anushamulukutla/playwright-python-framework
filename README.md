# SauceDemo Playwright Automation

## Project Overview

This project contains automated UI tests for the SauceDemo web application using Python, Playwright, and pytest.

The goal of this project is to build a maintainable and reliable UI automation framework while practicing real-world QA automation and testing practices.

## Technology Stack

* Python
* Playwright
* pytest
* pytest-playwright

## Project Structure

```text
saucedemo-playwright/
│
├── tests/
│   └── login_test.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

Make sure the following are installed:

* Python 3
* pip

## Installation

Clone the repository and navigate to the project directory.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running Tests

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/login_test.py
```

## Application Under Test

SauceDemo:

https://www.saucedemo.com/

## Test Coverage

Current automation coverage includes:

* Login page validation

Additional areas such as login scenarios, product catalog, shopping cart, and checkout will be added as the automation framework evolves.

## Team

* Anusha — QA Automation Engineer
* Mahsa — QA Automation Engineer

