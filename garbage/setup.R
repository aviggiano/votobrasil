setup <- function(consumerKey, consumerSecret) {
      reqURL <- "https://api.twitter.com/oauth/request_token"
      accessURL <- "http://api.twitter.com/oauth/access_token"
      authURL <- "http://api.twitter.com/oauth/authorize"
      twitCred <- OAuthFactory$new(consumerKey=consumerKey,
                                    consumerSecret=consumerSecret,
                                    requestURL=reqURL,
                                    accessURL=accessURL,
                                    authURL=authURL)     
}

oauth <- function() {
      twitCred$handshake() 
      registerTwitterOAuth(twitCred)
}