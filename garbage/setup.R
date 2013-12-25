setup <- function(consumerKey, consumerSecret) {
      library("ROAuth")
      library("twitteR")

      reqURL <- "https://api.twitter.com/oauth/request_token"
      accessURL <- "http://api.twitter.com/oauth/access_token"
      authURL <- "http://api.twitter.com/oauth/authorize"
      twitCred <- OAuthFactory$new(consumerKey=consumerKey,
                                    consumerSecret=consumerSecret,
                                    requestURL=reqURL,
                                    accessURL=accessURL,
                                    authURL=authURL)     
}

setup_tm <- function() {
     library("wordcloud")
     library("tm")
}

oauth <- function() {
      twitCred$handshake() 
      registerTwitterOAuth(twitCred)
}