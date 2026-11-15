#!/bin/bash
# Ping IndexNow (Bing, Yandex, etc.) with every sitemap URL, or the URLs given. Use only after launch on whichcabin.com.
KEY=6d99be0a8662d09dadd3f19d2857201e
cd "$(dirname "$0")"
if [ $# -gt 0 ]; then URLS=$(printf '"%s",' "$@"); else URLS=$(grep -o '<loc>[^<]*' sitemap.xml | sed 's/<loc>//' | sed 's/.*/"&"/' | paste -sd, -); fi
curl -s -o /dev/null -w "IndexNow HTTP %{http_code}\n" -H "Content-Type: application/json; charset=utf-8" https://api.indexnow.org/indexnow \
 -d "{\"host\":\"whichcabin.com\",\"key\":\"$KEY\",\"keyLocation\":\"https://whichcabin.com/$KEY.txt\",\"urlList\":[${URLS%,}]}"
