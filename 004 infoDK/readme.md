# Text message that I hhave won a lottery

**Medium:** Text message
** Content:** Vi forsøger at få fat i angående gevinster fra juni-trækningen(NET5820,30/06/2021). Saml den her: http://a.nn4y.com/SqNRZ 

## Redirect chain
1. http://a.nn4y.com/SqNRZ
    * **Action:** Redirect
    * **HTTP status code:** 302
2. https://track.plkitrck.com/734d64aa-1bb5-425e-a29f-fffec56c60ce
    * **Action:** Redirect
    * **HTTP status code:** 302
3. https://gift2you.live/netto/?cep=mVN7ul3OgexWAoKUFqdCm9_XEyITlPa3qqK3UrFaQaNxf5KCe4CJEPxULMq_Bvllp-mkeQqkVR5dHki805-5CweVktzGgy-TE06z-gOu21G681Plz8HBeuNZMILxWiJ9ranYneD0B5zCQGQtuU8j2-a2i-5nwsZUaW7i3memkxWn8SHamj-NePPn_GA8imC9N2BeaJcG3IWYNwYSRhhqOdMGBjQ7AXKw7hKMh3NznEcDx8FY4iHsP2h-2gfMEj-XiswxC2JqtFITbo9x90WoENAt2KCoSKB9uHal8fIymGJlnu0GhUEgltr1DxBhcgORyUIEkTPexbZp9aQYWOCokCBShSmRRyMA34b0iza-qjA&lptoken=1698254151db39f025bd
    * **Action:** Draw of random gift and Email
    * **HTTP status code:** 200
4. https://track.plkitrck.com/click
   * **Action:** Redirect
    * **HTTP status code:** 302
5. https://www.gmmsafeads.com/XNFTQ/XCQZJ/?uid=1619&sub3=158157572&sub1=100291&sub2=
   * **Action:** Redirect
    * **HTTP status code:** 302
6. https://luckywinnerisyou.com/o/205DFC28?clickid=a2ac3127e037417db87466a94fcc8817&subid=100291&sourceid=&data=199.48.45.35.103.219.251.164.22.1846646254.1626120737.1586856147
   * **Action:** Redirect
    * **HTTP status code:** 302
7. https://luckywinnerisyou.com/public_api/basic/v1/site/payment/partial_form_data 
   * **Action:** input postal and email addresses and phone number
    * **HTTP status code:** 200
8. https://luckywinnerisyou.com/public_api/basic/v1/site/payment/subscribe
   * **Action:** input card details and date of birth
    * **HTTP status code:** 200
9. https://aacsw.3ds.verifiedbyvisa.com/aacs/pahandler?vgtli=0021197001061424000783730420000000000000;vgp=eNpNjl0LgjAUhu%2F9FbL73DKzguPEEYkgfZl1PeaKSLfSFP33FSvo3D3v88J7IOyr0u5k3Vy1CtDYIciWSujiqi4Byg%2Br0RzZzZOrgpdayQANskEhteAYU8t%2BH3DxYMmaep5PyBzwF42rZJ0sqTv2yWzhEcCGjftu0vek4wL%2BoZH3WvcDjaKcRVvRplkmTtOhq%2FLD%2FrRhbNLuAsCmY%2Fo3fr7xVAteShqnGxalgP8zC%2FDn4Rd55kYq.DF8A9FE6
   * **Action:** Real Visa verified by visa  
    * **HTTP status code:** 200
10. https://securepaym.com/api/external/checkTransaction/64e76e92-e355-11eb-9127-7662b0575ec0
   * **Action:** checks whether you have entered your 2FA  
    * **HTTP status code:** 200
11. https://luckywinnerisyou.com/payment/fail?&paymentTransactionId=64e76e92-e355-11eb-9127-7662b0575ec0&errorMsg=transaction%20declined%20by%20authorization%20system
   * **Action:** failure page if 2FA fails  
    * **HTTP status code:** 200
    


## Curl dumps from burpsuite
I ran into a snag. The payment gateway was apparently real. at least the call to verified by visa seems to be legitimate, even though i would have expected to see a redirect to some https://nets.eu site for 3dSecure.  
This is basically a dump from BurpSuite with the details of the calls to the two urls that were getting data from the user. since the visa seems legitimate, I have issued abuse notices regarding the sites to cludflare and aws instead of proceeding.

### Send name and address
```sh
curl -i -s -k -X $'POST' \
    -H $'Host: luckywinnerisyou.com' -H $'Connection: close' -H $'Content-Length: 1907' -H $'sec-ch-ua: \";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"' -H $'Accept: application/json, text/plain, */*' -H $'sec-ch-ua-mobile: ?0' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H $'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryMkYwkZiBoKt0Zdus' -H $'Origin: https://luckywinnerisyou.com' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Dest: empty' -H $'Referer: https://luckywinnerisyou.com/' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' \
    -b $'PHPSESSID=hru876ak4g22jbfv8gkvlen68k; _ga=GA1.2.678851835.1626120825; _gid=GA1.2.551122589.1626120825' \
    --data-binary $'------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"from\"\x0d\x0a\x0d\x0aLpDomains\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"lang\"\x0d\x0a\x0d\x0adk\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"current_domain\"\x0d\x0a\x0d\x0aluckywinnerisyou.com\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"browserData\"\x0d\x0a\x0d\x0a{\"browserJavaEnabled\":false,\"browserLanguage\":\"en-US\",\"browserColorDepth\":\"24\",\"browserScreenWidth\":\"1927\",\"browserScreenHeight\":\"1336\",\"browserTZ\":\"240\",\"browserUserAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36\"}\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"country\"\x0d\x0a\x0d\x0aDenmark\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"clickid\"\x0d\x0a\x0d\x0aa2ac3127e037417db87466a94fcc8817\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"subid\"\x0d\x0a\x0d\x0a100291\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"offerid\"\x0d\x0a\x0d\x0a205DFC28\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"firstName\"\x0d\x0a\x0d\x0aJaxton\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"lastName\"\x0d\x0a\x0d\x0aS\xc3\xb8rensen\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"address\"\x0d\x0a\x0d\x0aStationsvej 1\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"zipCode\"\x0d\x0a\x0d\x0a2300\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"city\"\x0d\x0a\x0d\x0aK\xc3\xb8benhavn S\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"phone\"\x0d\x0a\x0d\x0a45 87629175\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus\x0d\x0aContent-Disposition: form-data; name=\"email\"\x0d\x0a\x0d\x0alikir38851@eyeremind.com\x0d\x0a------WebKitFormBoundaryMkYwkZiBoKt0Zdus--\x0d\x0a' \
    $'https://luckywinnerisyou.com/public_api/basic/v1/site/payment/partial_form_data'
```

### Send credit card information
```sh
curl -i -s -k -X $'POST' \
    -H $'Host: luckywinnerisyou.com' -H $'Connection: close' -H $'Content-Length: 3067' -H $'sec-ch-ua: \";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"' -H $'sec-ch-ua-mobile: ?0' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H $'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryjidW2HeLIBSVL1LD' -H $'Accept: */*' -H $'Origin: https://luckywinnerisyou.com' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: cors' -H $'Sec-Fetch-Dest: empty' -H $'Referer: https://luckywinnerisyou.com/' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' \
    -b $'PHPSESSID=hru876ak4g22jbfv8gkvlen68k; _ga=GA1.2.678851835.1626120825; _gid=GA1.2.551122589.1626120825' \
    --data-binary $'------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"from\"\x0d\x0a\x0d\x0aLpDomains\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"lang\"\x0d\x0a\x0d\x0adk\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"current_domain\"\x0d\x0a\x0d\x0aluckywinnerisyou.com\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"cardNumber\"\x0d\x0a\x0d\x0a4571 3628 1860 8817\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"expirationMonth\"\x0d\x0a\x0d\x0a07\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"expirationYear\"\x0d\x0a\x0d\x0a2021\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"cvv2\"\x0d\x0a\x0d\x0a480\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"bin\"\x0d\x0a\x0d\x0a{\"number\":{\"length\":16,\"luhn\":true},\"scheme\":\"visa\",\"type\":\"debit\",\"brand\":\"Traditional\",\"prepaid\":false,\"country\":{\"numeric\":\"208\",\"alpha2\":\"DK\",\"name\":\"Denmark\",\"emoji\":\"\xf0\x9f\x87\xa9\xf0\x9f\x87\xb0\",\"currency\":\"DKK\",\"latitude\":56,\"longitude\":10},\"bank\":null}\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"browserData\"\x0d\x0a\x0d\x0a{\"browserJavaEnabled\":false,\"browserLanguage\":\"en-US\",\"browserColorDepth\":\"24\",\"browserScreenWidth\":\"1927\",\"browserScreenHeight\":\"1336\",\"browserTZ\":\"240\",\"browserUserAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36\"}\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"country\"\x0d\x0a\x0d\x0aDenmark\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"clickid\"\x0d\x0a\x0d\x0aa2ac3127e037417db87466a94fcc8817\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"subid\"\x0d\x0a\x0d\x0a100291\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"sourceid\"\x0d\x0a\x0d\x0a\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"offerid\"\x0d\x0a\x0d\x0a205DFC28\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"firstName\"\x0d\x0a\x0d\x0aJaxton\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"lastName\"\x0d\x0a\x0d\x0aS\xc3\xb8rensen\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"address\"\x0d\x0a\x0d\x0aStationsvej 1\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"zipCode\"\x0d\x0a\x0d\x0a2300\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"city\"\x0d\x0a\x0d\x0aK\xc3\xb8benhavn S\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"phone\"\x0d\x0a\x0d\x0a45 87629175\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"email\"\x0d\x0a\x0d\x0alikir38851@eyeremind.com\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"numberCard\"\x0d\x0a\x0d\x0a4571 3628 1860 8817\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"expirynew\"\x0d\x0a\x0d\x0a07 / 21\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD\x0d\x0aContent-Disposition: form-data; name=\"cvcnew\"\x0d\x0a\x0d\x0a480\x0d\x0a------WebKitFormBoundaryjidW2HeLIBSVL1LD--\x0d\x0a' \
    $'https://luckywinnerisyou.com/public_api/basic/v1/site/payment/subscribe'
```


### Verify??
```sh
curl -i -s -k -X $'POST' \
    -H $'Host: aacsw.3ds.verifiedbyvisa.com' -H $'Connection: close' -H $'Content-Length: 686' -H $'Cache-Control: max-age=0' -H $'sec-ch-ua: \";Not A Brand\";v=\"99\", \"Chromium\";v=\"88\"' -H $'sec-ch-ua-mobile: ?0' -H $'Upgrade-Insecure-Requests: 1' -H $'Origin: https://luckywinnerisyou.com' -H $'Content-Type: application/x-www-form-urlencoded' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Sec-Fetch-Site: cross-site' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-Dest: document' -H $'Referer: https://luckywinnerisyou.com/' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' \
    --data-binary $'MD=aWQtOTkzNjE0Njg2MzExICAgICA%3D&PaReq=eJxUkk9v2zAMxb9K0XtDSXGdOGAIKI63%2BZCs3QoM2E2ViUTtLKeyPKT59IMyp3984o9%2BeHoUhQ%2F7wLz%2ByXYITLjhvjc7vnLN8to1N0UxzWWWz%2FOplNeEd%2FoHvxD%2B5dC7zpOciIlCuCBuONi98ZHQm5apuim7tuVgGeHcQNsNPoZXUrcC4QLYcqjXpGQuZkUmEP4zDuEP7WM89AuAadM7H3kXTOzC5NHFx8E%2Bc5y4DhCSEI19WdVbyrJciDnCiAjvme6GVPVMeHQNmV%2F38fvD82n7VInt005tTtWxLvWuLvUSISmwMZFJCSXFTKorJReiWCTvcx9Nm%2FKTLG4RxhoP6Qj94cfHBtohBPb2lYrZHOGNkI%2BHzrOPpBDeaoT3vOW3NJ%2BN9Zp0Wf22uvr6pbzXq2x7WpX68i3T1GdRcnTpmqWYnS0TICQbGFcI46IJ4dMD%2BBcAAP%2F%2F8dutbQ%3D%3D&TermUrl=https%3A%2F%2Fsecurepaym.com%2Fapi%2FparesResponse%2F64e76e92-e355-11eb-9127-7662b0575ec0%3FX-REQUEST-ID%3Db1bac47c32e7d1cad2d04b1fa9cc574a' \
    $'https://aacsw.3ds.verifiedbyvisa.com/aacs/pahandler?vgtli=0021197001061424000783730420000000000000;vgp=eNpNjl0LgjAUhu%2F9FbL73DKzguPEEYkgfZl1PeaKSLfSFP33FSvo3D3v88J7IOyr0u5k3Vy1CtDYIciWSujiqi4Byg%2Br0RzZzZOrgpdayQANskEhteAYU8t%2BH3DxYMmaep5PyBzwF42rZJ0sqTv2yWzhEcCGjftu0vek4wL%2BoZH3WvcDjaKcRVvRplkmTtOhq%2FLD%2FrRhbNLuAsCmY%2Fo3fr7xVAteShqnGxalgP8zC%2FDn4Rd55kYq.DF8A9FE6'
```