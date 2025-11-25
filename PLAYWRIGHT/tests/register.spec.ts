import { test, expect } from '@playwright/test';

test('registers a new user and verifies default balance', async ({ page }) => {
  try {
    // Step 1: Open the page
    await page.goto('https://czechibank.ostrava.digital');

    // Step 2: Switch to dark mode
    await page.getByRole('button', { name: 'Toggle theme' }).click();
    await page.getByRole('menuitem', { name: 'Dark' }).click();

    // Step 3: Click Register button
    await page.getByRole('button', { name: 'Register' }).click();
    await page.waitForURL('**/register');

    // Step 4: Generate RANDOM Full Name and fill it in
    const randomName = generateRandomFullName();
    await page.getByRole('textbox', { name: 'Full name *' }).fill(randomName);

    // Step 5: Generate email based on Full Name and fill it
    const email = generateEmailFromName(randomName);
    await page.getByRole('textbox', { name: 'Email *' }).fill(email);

    // Step 6: Generate random password and fill both password fields
    const password = generateRandomPassword();
    await page.getByRole('textbox', { name: 'Password *', exact: true }).fill(password);
    await page.getByRole('textbox', { name: 'Confirm Password *' }).fill(password);

    // Step 7: Wait 2 seconds
    await page.waitForTimeout(2000);

    // Step 8: Click Register button
    await page.getByRole('button', { name: 'Register' }).click();

    // Step 9: Validate that registration was successful and continue to the app
    await page.waitForURL('**/register/success');
    await expect(page.getByRole('heading', { name: 'Registration Successful!' })).toBeVisible();
    await page.getByRole('button', { name: 'Continue to the app' }).click();
    await page.waitForURL('**/');

    // Step 10: Validate that user's default account balance is 100000.0 Czechitokens
    await expect(page.getByRole('heading', { name: /Czechitoken 100000\.0/ })).toBeVisible();
    const balanceText = await page.getByRole('heading', { name: /Czechitoken 100000\.0/ }).textContent();
    expect(balanceText).toContain('100000.0');

    // Step 11: Close the current browser tab
    await page.close();
  } catch (error) {
    // Step 12: If any error occurs during the process, close current active window
    try {
      await page.close();
    } catch (closeError) {
      // Silently ignore if already closed
    }
    throw error;
  }
});

function generateRandomFullName(): string {
  const firstNames = ['James', 'John', 'Michael', 'Robert', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles'];
  const lastNames = ['Morrison', 'Anderson', 'Thompson', 'Martinez', 'Garcia', 'Robinson', 'Clark', 'Rodriguez', 'Lewis', 'Walker'];
  
  const firstName = firstNames[Math.floor(Math.random() * firstNames.length)];
  const lastName = lastNames[Math.floor(Math.random() * lastNames.length)];
  
  return `${firstName} ${lastName}`;
}

function generateEmailFromName(fullName: string): string {
  const [firstName, lastName] = fullName.split(' ');
  const randomNum = Math.floor(Math.random() * 10000);
  return `${firstName.toLowerCase()}.${lastName.toLowerCase()}.${randomNum}@example.com`;
}

function generateRandomPassword(): string {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*';
  let password = '';
  for (let i = 0; i < 12; i++) {
    password += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return password;
}
