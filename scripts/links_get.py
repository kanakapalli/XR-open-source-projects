from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Set up WebDriver
driver = webdriver.Chrome()  # Use the appropriate WebDriver (e.g., ChromeDriver)
driver.maximize_window()

# Base URL for the project gallery
base_url = "https://xr-midwest.devpost.com/project-gallery?page="

# Output CSV file
output_file = 'project_details_with_description.csv'
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Project Name", "Short Description", "Project URL", "Try it Out Links"])

    # Iterate through all pages
    page_number = 1
    while True:
        print(f"Processing page {page_number}...")
        driver.get(base_url + str(page_number))
        time.sleep(3)  # Allow page to load

        # Find all project cards on the page
        project_cards = driver.find_elements(By.CLASS_NAME, "gallery-item")
        if not project_cards:
            print("No more projects found. Exiting.")
            break

        for card in project_cards:
            try:
                # Get project name and link
                project_name = card.find_element(By.TAG_NAME, "h5").text
                project_url = card.find_element(By.CLASS_NAME, "link-to-software").get_attribute("href")

                # Open the project page in a new tab
                driver.execute_script("window.open(arguments[0]);", project_url)
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(3)  # Allow project page to load

                # Extract project description
                try:
                    description = driver.find_element(By.CSS_SELECTOR, "header.page-header p.large").text
                except:
                    description = "No description available"

                # Extract "Try it out" links
                try_it_out_section = driver.find_elements(By.XPATH, "//h2[text()='Try it out']")
                if try_it_out_section:
                    links_section = driver.find_element(By.XPATH, "//ul[@data-role='software-urls']")
                    links = links_section.find_elements(By.TAG_NAME, "a")
                    try_it_out_links = [link.get_attribute("href") for link in links]
                    try_it_out_links_str = ", ".join(try_it_out_links)
                else:
                    try_it_out_links_str = "No links available"

                # Write to CSV
                print(f"Found project: {project_name}")
                writer.writerow([project_name, description, project_url, try_it_out_links_str])

                # Close the project tab and switch back to the gallery
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            except Exception as e:
                print(f"Error processing project: {e}")
                driver.switch_to.window(driver.window_handles[0])
                continue

        # Proceed to the next page
        page_number += 1

driver.quit()
print(f"Data extraction complete. Results saved to {output_file}.")
