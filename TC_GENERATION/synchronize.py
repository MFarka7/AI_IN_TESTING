import requests
import json

# --- Configuration ---
ZEPHYR_SCALE_BASE_URL = "https://api.zephyrscale.smartbear.com/v2" # Or your Jira base URL for server deployments
JIRA_BASE_URL = "https://your-jira-instance.atlassian.net" # Replace with your Jira base URL
API_TOKEN = "<YOUR_ZEPHYR_SCALE_API_TOKEN>" # Replace with your Zephyr Scale API token
PROJECT_KEY = "<YOUR_PROJECT_KEY>" # Replace with your Jira Project Key

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# --- Test Cases and Steps Data (from the JSON generated above) ---
test_cases_data = [
  {
    "testCase": {
      "name": "Successful User Registration - Valid Email and Password"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter a valid email address.",
            "testData": "testuser@example.com",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Enter a valid password (6+ chars, 1 small, 1 capital).",
            "testData": "Password123",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "User is successfully registered and redirected to a confirmation page or dashboard."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Invalid Email Format (Missing @)"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter an email address missing '@'.",
            "testData": "invalidemail.com",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Enter a valid password.",
            "testData": "ValidPass1",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "An error message indicating 'Invalid email format' or similar is displayed below the email field. User is not registered."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Invalid Email Format (Missing Domain)"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter an email address missing a domain.",
            "testData": "user@",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Enter a valid password.",
            "testData": "ValidPass1",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "An error message indicating 'Invalid email format' or similar is displayed below the email field. User is not registered."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Invalid Email Format (Empty Email)"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Leave the email field empty.",
            "testData": "'' (empty string)",
            "expectedResult": "The email field remains empty."
          }
        },
        {
          "inline": {
            "description": "Enter a valid password.",
            "testData": "ValidPass1",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "An error message indicating 'Email is required' or similar is displayed below the email field. User is not registered."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Password Too Short (Less than 6 characters)"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter a valid email address.",
            "testData": "testuser@example.com",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Enter a password less than 6 characters long.",
            "testData": "Pass1",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "An error message indicating 'Password must be at least 6 characters long' or similar is displayed below the password field. User is not registered."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Password Missing Small Letter"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter a valid email address.",
            "testData": "testuser@example.com",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Enter a password missing a small letter.",
            "testData": "PASSWORD123",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "An error message indicating 'Password must contain at least one small letter' or similar is displayed below the password field. User is not registered."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Password Missing Capital Letter"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter a valid email address.",
            "testData": "testuser@example.com",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Enter a password missing a capital letter.",
            "testData": "password123",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "An error message indicating 'Password must contain at least one capital letter' or similar is displayed below the password field. User is not registered."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Empty Password Field"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter a valid email address.",
            "testData": "testuser@example.com",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Leave the password field empty.",
            "testData": "'' (empty string)",
            "expectedResult": "The password field remains empty."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "An error message indicating 'Password is required' or similar is displayed below the password field. User is not registered."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Both Email and Password Invalid"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter an invalid email address.",
            "testData": "invalid",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Enter an invalid password (e.g., too short).",
            "testData": "short",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "Error messages for both invalid email and invalid password are displayed. User is not registered."
          }
        }
      ]
    }
  },
  {
    "testCase": {
      "name": "Registration Failure - Existing Email Address"
    },
    "testSteps": {
      "mode": "APPEND",
      "items": [
        {
          "inline": {
            "description": "Navigate to the registration page.",
            "testData": "URL of the registration page",
            "expectedResult": "The registration form is displayed."
          }
        },
        {
          "inline": {
            "description": "Enter an email address that is already registered.",
            "testData": "existinguser@example.com",
            "expectedResult": "The email field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Enter a valid password.",
            "testData": "ValidPass1",
            "expectedResult": "The password field accepts the input."
          }
        },
        {
          "inline": {
            "description": "Click the 'Register' or 'Submit' button.",
            "testData": "N/A",
            "expectedResult": "An error message indicating 'Email address already in use' or similar is displayed. User is not registered."
          }
        }
      ]
    }
  }
]


def create_test_case_and_steps(test_case_data, test_steps_data):
    """
    Creates a test case in Zephyr Scale and uploads its inline test steps.
    """
    # 1. Create the Test Case
    create_tc_url = f"{ZEPHYR_SCALE_BASE_URL}/testcases"
    tc_payload = {
        "projectKey": PROJECT_KEY,
        "name": test_case_data["name"],
        "labels": ["registration"] # Example label
    }

    print(f"Creating test case: {test_case_data['name']}...")
    try:
        response = requests.post(create_tc_url, headers=HEADERS, data=json.dumps(tc_payload))
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        test_case_key = response.json().get("key")
        print(f"Successfully created test case: {test_case_key}")
    except requests.exceptions.RequestException as e:
        print(f"Error creating test case '{test_case_data['name']}': {e}")
        if response is not None:
            print(f"Response content: {response.content.decode()}")
        return

    # 2. Upload Inline Test Steps
    upload_steps_url = f"{ZEPHYR_SCALE_BASE_URL}/testcases/{test_case_key}/teststeps"
    steps_payload = test_steps_data # Already in the correct format

    print(f"Uploading steps for test case: {test_case_key}...")
    try:
        response = requests.post(upload_steps_url, headers=HEADERS, data=json.dumps(steps_payload))
        response.raise_for_status()
        print(f"Successfully uploaded steps for test case: {test_case_key}")
    except requests.exceptions.RequestException as e:
        print(f"Error uploading steps for test case '{test_case_key}': {e}")
        if response is not None:
            print(f"Response content: {response.content.decode()}")

# --- Main execution ---
if __name__ == "__main__":
    for tc in test_cases_data:
        create_test_case_and_steps(tc["testCase"], tc["testSteps"])
