import { test, expect } from '@playwright/test';

test('Complete registration flow on CzechiBank', async ({ page }) => {
  try {
    // Step 1: Open the page
    await page.goto('https://czechibank.ostrava.digital');

    // Step 2: Switch to dark mode
    await page.getByRole('button', { name: 'Toggle theme' }).click();
    await page.getByRole('menuitem', { name: 'Dark' }).click();

    // Step 3: Click Register button
    await page.getByRole('button', { name: 'Register' }).click();

    // Step 4-6: Generate random data and fill the form
    const timestamp = Date.now();
    const fullName = `Test User ${timestamp}`;
    const email = `testuser${timestamp}@example.com`;
    const password = `SecurePass${timestamp}!`;

    await page.getByRole('textbox', { name: 'Full name *' }).fill(fullName);
    await page.getByRole('textbox', { name: 'Email *' }).fill(email);
    await page.getByRole('textbox', { name: 'Password *', exact: true }).fill(password);
    await page.getByRole('textbox', { name: 'Confirm Password *' }).fill(password);

    // Step 7: Wait 2 seconds
    await page.waitForTimeout(2000);

    // Step 8: Click Register button
    await page.getByRole('button', { name: 'Register' }).click();

    // Step 9: Validate that registration was successful
    await expect(page.getByRole('heading', { name: 'Registration Successful!' })).toBeVisible();
    
    // Continue to the app
    await page.getByRole('button', { name: 'Continue to the app' }).click();

    // Step 10: Validate user's default account balance is 100000.0 Czechitokens
    await expect(page.getByRole('heading', { name: /Czechitoken 100000\.0/ })).toBeVisible();
    
    // Also validate the greeting with user name
    await expect(page.getByRole('heading', { name: `Hello ${fullName}!` })).toBeVisible();

  } catch (error) {
    // Step 12: If any error occurs, close the browser
    await page.close();
    throw error;
  }

  // Step 11: Close the current browser tab
  await page.close();
});
