"use strict";

// This is the global list of the stories, an instance of StoryList
let storyList;
let favoriteList = [];

/** Get and show stories when site first loads. */

async function getAndShowStoriesOnStart() {
  storyList = await StoryList.getStories();
  $storiesLoadingMsg.remove();

  putStoriesOnPage();
}

async function getFavoriteList(){
  console.debug("getFavoriteList");
  const res = await axios.get(`${BASE_URL}/users/${currentUser.username}?token=${currentUser.loginToken}`)
  const resObjList = res.data.user.favorites
  favoriteList = []
  
  for(let story in resObjList){
    favoriteList.push(resObjList[story].storyId)
  }
  
}
/**
 * A render method to render HTML for an individual Story instance
 * - story: an instance of Story
 *
 * Returns the markup for the story.
 */

function generateStoryMarkup(story) {
  console.debug("generateStoryMarkup", story);
  const hostName = story.getHostName();
  return $(`
      <li id="${story.storyId}">
        <a href="${story.url}" target="a_blank" class="story-link">
          ${story.title}
        </a>
        <small class="story-hostname">(${hostName})</small>
        <small class="story-author">by ${story.author}</small>
        <small class="story-user">posted by ${story.username}</small>
        ${favoriteButtonMarkup(story)}
        ${removeButtonMarkup(story)}
      </li>
    `);
}

function favoriteButtonMarkup(story){
  //uncomment for debug info
  //console.debug("favoriteButtonMarkup", story);
  if(currentUser){
    return `<button class="story-favorite-button">  <small style="padding:1px">${favoriteList.includes(story.storyId) ? "unfavorite" : "favorite"}</small>  </button>`;
  }
  else{
    return '';
  }
}

function favoriteButtonAddListener(){
  console.debug("favoriteButtonAddListener");
  $(".story-favorite-button").on("click", favoriteHandle)
}

function removeButtonMarkup(story){
  
  //console.debug("removeButtonMarkup", story);
  if(currentUser){
    if(currentUser.ownStories.find(x => x.storyId == story.storyId) ){
    return `<button class="story-remove-button">  <small style="padding:1px">remove</small>  </button>`
    }
    return ''
  }
  else{
    return ''
  }
}

function removeButtonAddListener(){
  $(".story-remove-button").on("click", function(e){
    console.log($(this).parent().attr('id'))
    removeStory($(this).parent().attr('id'))  
    $(this).parent().remove();
  })
}


/** Gets list of stories from server, generates their HTML, and puts on page. */

async function putStoriesOnPage() {
  console.debug("putStoriesOnPage");

  $allStoriesList.empty();
  // loop through all of our stories and generate HTML for them
  for (let story of storyList.stories) {
    const $story = generateStoryMarkup(story);
    $allStoriesList.append($story);

  }
  favoriteButtonAddListener();
  removeButtonAddListener();
  $allStoriesList.show();
}

function putFavoriteStoriesOnPage() {
  console.debug("putFavoriteStoriesOnPage");

  $allStoriesList.empty();

  // loop through all of our stories and generate HTML for them
  for (let story of storyList.stories) {
    if(favoriteList.includes(story.storyId)){
    const $story = generateStoryMarkup(story);
    $allStoriesList.append($story);
    }
  }

  $allStoriesList.show();
}

/** sadasd */
async function submitStory(){
  const title = $storyTitle.val();
  const author = $storyAuthor.val();
  const url = $storyUrl.val();
  
  const storyData = { title, author, url }
  
  await storyList.addStory(currentUser, storyData);
  storyList = await StoryList.getStories();

}

$storyForm.on("submit", function(e){
  e.preventDefault();
  submitStory();
  hidePageComponents();
  putStoriesOnPage();
})

/**
 * 
 *{  const res = await axios.get(`${BASE_URL}/users/${currentUser.username}/favorites/${id}?token=${currentUser.loginToken}`, {
    token: currentUser.loginToken
  })
}
 */
async function addFavoriteStory(id){
  console.debug("addFavoriteStory");
  const res = await axios.post(`${BASE_URL}/users/${currentUser.username}/favorites/${id}`, {
    token: currentUser.loginToken
  });
}

async function removeFavoriteStory(id){
  console.debug("removeFavoriteStory");
  const res = await axios.delete(`${BASE_URL}/users/${currentUser.username}/favorites/${id}`, {
    data: { token: currentUser.loginToken}
  });
}

async function removeStory(id){
  console.debug("removeStory");
  const res = await axios.delete(`${BASE_URL}/stories/${id}`, {
    data: { token: currentUser.loginToken}
  });
}

function favoriteHandle(e){
  const id = $(this).parent().attr("id")
  const favoriteState = $(this).children().text()

  console.log(favoriteState)
  console.log(favoriteState == " favorite ")
  switch(favoriteState){
    case "favorite": {
      addFavoriteStory(id);
      favoriteList.push(id);
      $(this).children().text("unfavorite");
      break;
    }
    case "unfavorite":{
      removeFavoriteStory(id);
      favoriteList = favoriteList.filter(e => e !== id);
      $(this).children().text("favorite");
      console.log('unfavre')
      break;
    }
    default: {
      console.debug("favoriteButtonHandle default")
    }
  }

  console.log(favoriteState)
}


async function getUserData(){
  const res = await axios.get(`${BASE_URL}/users/${currentUser.username}?token=${currentUser.loginToken}`)
  console.log(res)
}

