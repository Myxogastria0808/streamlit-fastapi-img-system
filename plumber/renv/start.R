dir_path <- paste0(getwd(), "/", "start.R")
pr <- plumber::plumb(dir_path)$run(host = "127.0.0.1", port = 8000)
