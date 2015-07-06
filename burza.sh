curl "https://burze.dzis.net/?page=wyszukiwarka" -H "Cookie: sesja=48503c38bfe63b99f98a9a64772be2f4; session=1; PHPSESSID=q2cn3a9i4p3fkjlpigu20kdm87" -H "Origin: https://burze.dzis.net" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36" -H "Content-Type: application/x-www-form-urlencoded" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Cache-Control: max-age=0" -H "Referer: https://burze.dzis.net/?page=wyszukiwarka" -H "Connection: keep-alive" --data "miejscowosc=Gorz"%"C3"%"B3w+Wielkopolski&y=52.44&x=15.14&promien=20" --compressed > burza
sed -n "/<div class=/,/<\/div>/p" burza > a
sed 's/<[^>]\+>//g' a > burza
sed '/^\s*$/d' burza > a
sed  '4,10d'  a > pliki/burza
rm a 
rm burza
#cat pliki/burza
