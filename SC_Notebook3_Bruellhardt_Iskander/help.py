### Your code here...
post = 'https://dribbble.com/shots/25765540-Bold-Bean-Coffee-Roasters-Bag-Label'

browser.get("https://dribbble.com")
    
post_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shot-thumbnail-link")))
wait()
post_link.click()
wait()

feedback = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Feedback')]")))
feedback.click()
wait()

comments_stuff = driver.find_elements(By.CSS_SELECTOR, "div.shot-comment")


title = driver.find_element(By.CSS_SELECTOR, "h1.shot-header__title").text
    
    
author_stuff = driver.find_element(By.CSS_SELECTOR, "a.hoverable[rel='contact']")
name = author_stuff.text
username = author_elem.get_attribute("href").split('/')[-1]

scraped_comments = []
for comment in comments_stuff:
    try:
            commentator = comment.find_element(By.CSS_SELECTOR, "a.shot-comment-author").text
            comment_text = comment.find_element(By.CSS_SELECTOR, "div.shot-comment-text").text
            scraped_comments.append({commentator: comment_text})
    except:
        continue

print(f"""
    - Post title {title}
    - Post author (name) {name}
    - Post author (username) {username}
    - All the comments (commentor + comment text) {scraped_comments}""")