"use strict";

const $showsList = $("#shows-list");
const $episodesArea = $("#episodes-area");
const $searchForm = $("#search-form");


/** Given a search term, search for tv shows that match that query.
 *
 *  Returns (promise) array of show objects: [show, show, ...].
 *    Each show object should contain exactly: {id, name, summary, image}
 *    (if no image URL given by API, put in a default image URL)
 */

async function getShowsByTerm( searchTerm) {
  const res = await axios.get(`http://api.tvmaze.com/search/shows?q=${searchTerm}`)
  const shows = res.data
  const showList = []
  let addedImage;
  for(let show in shows){
    
    if(shows[show]["show"]["image"]){
      addedImage = shows[show]["show"]["image"]["medium"]  
    }
    else{
      addedImage = "https://store-images.s-microsoft.com/image/apps.65316.13510798887490672.6e1ebb25-96c8-4504-b714-1f7cbca3c5ad.f9514a23-1eb8-4916-a18e-99b1a9817d15?mode=scale&q=90&h=300&w=300"
    }
    showList.push({
      id: shows[show]["show"]["id"],
      name: shows[show]["show"]["name"],
      summary: shows[show]["show"]["summary"],
      image: addedImage
    })
  }
  console.log(showList)
  return showList
}


/** Given list of shows, create markup for each and to DOM */

function populateShows(shows) {
  $showsList.empty();

  for (let show of shows) {
    const $show = $(
        `<div data-show-id="${show.id}" class="Show col-md-12 col-lg-6 mb-4">
         <div class="media">
           <img 
              src="${show.image}" 
              alt="${show.name}" 
              class="w-25 mr-3">
           <div class="media-body">
             <h5 class="text-primary">${show.name}</h5>
             <div><small>${show.summary}</small></div>
             <button class="btn btn-outline-dark btn-sm Show-getEpisodes">
               Episodes
             </button>
           </div>
         </div>  
       </div>
      `);
    
    
    $showsList.append($show);  }
}


/** Handle search form submission: get shows from API and display.
 *    Hide episodes area (that only gets shown if they ask for episodes)
 */

async function searchForShowAndDisplay() {
  const term = $("#search-query").val();
  const shows = await getShowsByTerm(term);

  $episodesArea.hide();
  populateShows(shows);
}
  
$searchForm.on("submit", async function (evt) {
  evt.preventDefault();
  await searchForShowAndDisplay();
  await addEpisodeListeners();
});



/** Given a show ID, get from API and return (promise) array of episodes:
 *      { id, name, season, number }
 */

async function getEpisodesOfShow(id) {

    const res = await axios.get(`http://api.tvmaze.com/shows/${id}/episodes`)

    const episodes = res.data
    const episodeList = []
    for( let episode in episodes ){
      episodeList.push({
        id : episodes[episode]["id"],
        name : episodes[episode]["name"],
        season: episodes[episode]["season"],
        number: episodes[episode]["number"]

      })
    }
    console.log(episodeList)
    return episodeList;

 }

 

/** Given an array of (promise) episodes populate the episode region 
 * 
*/

async function populateEpisodes(episodeList) {
  
  const episodes = await episodeList;
  $("#episodes-area").show();
  $("#episodes-area").append("<ul> </ul>")
 
  //return if no episodes
  if(!episodes){
    return
  }

  for (let episode of episodes) {
    const episode2 = $(
        `<li>${episode.name} (season ${episode.season}, number ${episode.number}) </li>`
      );

    episode2.appendTo("#episodes-area");  }

 }

/** attach event listeners to the dynamically generated episode buttons
 * 
 */
async function addEpisodeListeners(){
  const episodeID = $(".Show").attr("data-show-id")
  const episodeList = getEpisodesOfShow(episodeID)
  
  $(".Show").each(function(){
      $(this).find("button").on("click", function(){
        populateEpisodes(episodeList)
      })}
    )
}