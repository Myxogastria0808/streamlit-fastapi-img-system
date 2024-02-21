library(plumber)


path <- paste0(getwd(), "/", "api.R")
plumber::plumb(path)$run(host = "127.0.0.1", port = 8000)
