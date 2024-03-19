def last_tab(driver):
  """Close all tabs except for the last tab.

  Args:
    driver: The WebDriver instance.
  """

  driver.execute_script(
      'window.open("about:blank", "_blank");')
  driver.switch_to.window(driver.window_handles[-1])
  for window_handle in driver.window_handles[:-1]:
    driver.switch_to.window(window_handle)
    driver.close()
  driver.switch_to.window(driver.window_handles[-1])
