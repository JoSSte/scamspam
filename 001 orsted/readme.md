# Scam mail 001

Fra Ørsted A/S <pos.noreply@oeiizk.waw.pl>

Inspired from https://github.com/engineer-man/youtube/blob/master/033 - credit goes to Engineerguy

## Redirect chain
1. https://u.to/xSJYGw
    * **Action:** Redirect
    * **HTTP status code:** 302
2. https://qoo.gl/DSFS345
    * **Action:** Redirect
    * **HTTP status code:** 302
3. https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/index.htm
    * **Action:** input card details and date of birth
    * **HTTP status code:** 200
4. https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/valider.php 
    * **Action:** stored card information
    * **HTTP status code:** 302
5. https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/NamID/NemID1.html 
    * **Action:** Input NemID information (potentially CPR/SSN)
    * **HTTP status code:** 200
6. https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/NamID/sr/s.php 
    * **Action:** Saving NemID information
    * **HTTP status code:** 302
7. https://ietarst-jansf7656.wpdevcloud.com/plugins/76g54fgf/24fhj23zet/jyukity68bf/gh65fdze43e/24qsfq24/NamID/NemID.html
    * **Action:** Dummy approval with nemid 2FA app, with inoperative link to use OTP card
    * **HTTP status code:** 200

Kudos to the support team at cloudaccess.net. Six minutes after I reported the site, it was taken down.