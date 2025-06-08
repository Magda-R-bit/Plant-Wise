# Manual Testing


## Navigation

| Feature                | Tested | Result |
| ---------------------- | ------ | ------ |
| Home > Shop            | ✅      | Pass   |
| Shop by Category       | ✅      | Pass   |
| View product details   | ✅      | Pass   |
| Logo redirects to Home | ✅      | Pass   |
| Cart/Checkout links    | ✅      | Pass   |

## Products & Shop

✅ All products display with price, name, image

✅ Category filtering (e.g., "Herbs", "Flowers") works

✅ Search bar functions correctly

✅ Product detail pages display all info and related deals



## Cart & Checkout

| Test                               | Result |
| ---------------------------------- | ------ |
| Add to cart                        | ✅      |
| View/update cart                   | ✅      |
| Remove item from cart              | ✅      |
| Proceed to checkout                | ✅      |
| Complete checkout with Stripe      | ✅      |
| Order confirmation email simulated | ✅      |
| Cart cleared after success         | ✅      |


## Deals Logic (Discounts & BOGO)

| Deal Type        | Test                                                          | Result |
| ---------------- | ------------------------------------------------------------- | ------ |
| Discount (%)     | Correct percentage displayed (e.g., “10% off applied!”)       | ✅      |
| BOGO             | Free item displayed & quantity updated (e.g., “+1 free!”)     | ✅      |
| Mixed cart logic | Discounts + BOGO combinations applied correctly               | ✅      |
| Checkout summary | Deal logic reflected in order summary and OrderLineItem model | ✅      |
| Database         | `applied_deal` stored and viewable in admin/order summary     | ✅      |


## Tips & Guides

### Viewing Tips

| Test Case                                      | Expected Result                           | Result |
| ---------------------------------------------- | ----------------------------------------- | ------ |
| Navigate to "Tips & Guides" from nav/menu      | Tips page loads with a list of entries    | ✅      |
| Click a guide title to view details            | Full content of the tip/guide is shown    | ✅      |
| Return to the list from individual guide view  | Link works and page returns without error | ✅      |
| Tips styled consistently (e.g., titles)        | Layout is clean and readable              | ✅      |


### Adding Tips

| Test Case                                    | Expected Result                                | Result                       |
| -------------------------------------------- | ---------------------------------------------- | ---------------------------- |
| Logged in user/admin sees "Submit a Tip" button   | Button is visible and functional               | ✅|
| Submit a form with valid title content and category      | Tip is added, confirmation shown | ✅                            |
| Submit with invalid data (e.g., empty title) | Error messages shown, form not submitted       | ✅                            |
| Added tip appears in list after refresh      | New tip appears at top or in correct order     | ✅                            |


## Wishlist

### Adding to Wishlist

| Test Case                                            | Expected Result                                     | Result |
| ---------------------------------------------------- | --------------------------------------------------- | ------ |
| While browsing, click "Add to Wishlist" on a product | Product appears in Wishlist page                    | ✅      |
| Same product added again                             | Not duplicated, user gets a message or it’s ignored | ✅      |
| Not logged-in user clicks "Add to Wishlist"          | Redirected to login or shown a message              | ✅      |


### Viewing Wishlist

| Test Case                                  | Expected Result                                      | Result |
| ------------------------------------------ | ---------------------------------------------------- | ------ |
| Click "Wishlist" icon in the navbar | Wishlist page opens, showing saved products (if any) | ✅      |
| Empty wishlist shows appropriate message   | Message like "You haven't added anything to your wishlist yet" is displayed   | ✅      |

### Removing from Wishlist

| Test Case                               | Expected Result                               | Result |
| --------------------------------------- | --------------------------------------------- | ------ |
| Click "Remove" on a product in wishlist | Product disappears from list, page refreshes  | ✅      |
| Remove item                             | List becomes empty with correct message shown | ✅      |

### Moving to Cart from Wishlist

| Test Case                                   | Expected Result                                        | Result |
| ------------------------------------------- | ------------------------------------------------------ | ------ |
| Click "Add to Cart" for product in wishlist | Product is added to cart, removed from wishlist | ✅      |
| Product already in cart                     | Quantity increases                   | ✅      |




## Error Pages

| Page | Trigger             | Image Loads | Custom Text                       | Result |
| ---- | ------------------- | ----------- | --------------------------------- | ------ |
| 404  | Invalid URL         | ✅ via S3    | ✅ Funny & useful                  | ✅      |
| 500  | `/test-error/` view | ✅ via S3    | ✅ "Houston, we have a problem..." | ✅      |


## User Authentication

| Feature        | Tested | Result      |
| -------------- | ------ | ----------- |
| Register       | ✅      | Pass        |
| Login/Logout   | ✅      | Pass        |
| Password Reset | ✅      | Pass        |
| Invalid Login  | ✅      | Error shown |
| Profile Page   | ✅      | Pass        |


## Profile & Order History

| Feature                      | Tested | Result |
| ---------------------------- | ------ | ------ |
| View previous orders         | ✅      | Pass   |
| Update saved address info    | ✅      | Pass   |
| Check previous deals applied | ✅      | Pass   |


## Form Testing


| Test Case                                      | Expected Result                           | Result |
| ---------------------------------------------- | ----------------------------------------- | ------ |
| Contact Form                                   | Form loads when all fields field in       | ✅     |



## Media (Images)

| Image Type     | Issue                      | Fix Applied                      | Result |
| -------------- | -------------------------- | -------------------------------- | ------ |
| Product images | Loaded from AWS S3         | Correct URLs & `MEDIA_URL` set   | ✅      |
| Static images  | Not shown in `DEBUG=False` | Used full S3 URLs / staticfiles  | ✅      |
| 404/500 images | Not appearing via CSS      | Moved to template or used inline | ✅      |



## Responsive Testing

**Tested using Chrome DevTools for:**

- iPhone SE, iPhone XR,

- iPad,

- MacBook Pro 13", Desktop Full HD

✅ All layouts adjust correctly, including:

- Header, footer responsiveness

- Grid system in product listings

- Checkout flow scaling properly




