library(plumber)


# Title
#* @apiTitle Sample API
# Description
#* @apiDescription This is a sample API
# TOS link
#* @apiTOS
# Contact object
#* @apiContact list(name = "Yuki Osada", url = "http://yukiosada.work/", email = "r.rstudio.c@gmail.com")
# License object
#* @apiLicense list(name = "Apache 2.0", url = "https://www.apache.org/licenses/LICENSE-2.0.html")
# Version
#* @apiVersion 0.0.1
# Tag Description
#* @apiTag sample Sample API


#* @filter cors
cors <- function(req, res) {
  res$setHeader("Access-Control-Allow-Origin", "*")
  if (req$REQUEST_METHOD == "OPTIONS") {
    res$setHeader("Access-Control-Allow-Methods", "GET")
    res$setHeader(
      "Access-Control-Allow-Headers",
      req$HTTP_ACCESS_CONTROL_REQUEST_HEADERS
    )
    res$status <- 200
    return(list())
  } else {
    plumber::forward()
  }
}

#* dataディレクトリ内のsvg画像を取得できる
#* @param generation 世代数を入力してください。
#* @param img 取得したい画像の番号を入力してください。
#* @serializer contentType list(type="image/svg+xml")
#* @get /generation/<generation:int>/img/<img:int>
function(generation, img) {
  file_path <- paste0(getwd(), "/data/", generation, "/", img, ".svg")
  readBin(file_path, "raw", n = file.info(file_path)$size)
}

#* dataディレクトリ内のディレクトリの一覧を取得できる
#* @get /archive
function() {
  root_dir <- getwd()
  root_archive_dir <- paste0(getwd(), "/archive")
  setwd(root_archive_dir)
  root_archive_dirs <- dir()
  result_list <- list()
  for (archive_dir in root_archive_dirs) {
    each_archive_dir <- paste0(root_archive_dir, "/", archive_dir)
    setwd(each_archive_dir)
    generation_dirs <- dir()
    result_list <- append(result_list, list(c(archive_dir, generation_dirs)))
  }
  setwd(root_dir)
  return(list(archive = result_list))
}

#* dataディレクトリ内のsvg画像を取得できる
#* @param generation 世代数を入力してください。
#* @param img 取得したい画像の番号を入力してください。
#* @serializer contentType list(type="image/svg+xml")
#* @get /archive/<dir_name>/generation/<generation:int>/img/<img:int>
function(dir_name, generation, img) {
  file_path <- paste0(getwd(), "/archive/", dir_name, "/", generation, "/", img, ".svg")
  readBin(file_path, "raw", n = file.info(file_path)$size)
}