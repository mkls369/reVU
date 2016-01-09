rm(list=ls())
set.seed(123)
#user rating data
dt_user_ratings <- data.frame(id = NA,	user_id = NA,	score = NA,	rating_id = NA)

user_ids <- rep(1:100, each = 8)
score <- sample(1:5, length(user_ids), replace=T)
rating_id <- c(replicate(length(unique(user_ids)), sample(1:16, 8, replace=F)))

# dt_user_ratings["user_ids"] <- user_ids
# dt_user_ratings["score"] <- score
# dt_user_ratings["rating_id"] <- rating_id

dt <- data.frame(id = 1:length(user_ids), user_ids, score, rating_id)

write.csv(dt, "D:/Users/Mykolas/winerama-recommender-tutorial/winerama/data/userratings.csv",
          row.names = F)
