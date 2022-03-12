// CHEKBOXS
const $eventMainCheckbox = document.getElementById("main-checkbox");
const userCheckboxs = document.getElementsByClassName('user-checkbox');
// BUTTONS
const $eventShareButton = document.getElementById("share-button");
//const downloadLink = document.getElementById("download-link");
const pdfDownloadLink = document.getElementById("pdf-download")
const jsonDownloadLink = document.getElementById("json-download")

// EVENTS
function enableAllCheckboxs(e) {
   if(e.target.checked) {
      for (let i=0; i<userCheckboxs.length; i++) {
         userCheckboxs[i].checked = true;
      }
   }
   else {
      for (let i=0; i<userCheckboxs.length; i++) {
         userCheckboxs[i].checked = false;
      }
   }
}
$eventMainCheckbox.addEventListener("change", enableAllCheckboxs);

function nextChargeShowLinks() {
   window.onload = function() {
      showDownloadLinks;
   }
}
function showDownloadLinks() {
   jsonDownloadLink.hidden = false;
   pdfDownloadLink.hidden = false;
}
$eventShareButton.addEventListener("click", showDownloadLinks);
/*
window.onload = function () { 

        newInvite();
        document.ag.src="b.jpg";
        jsonDownloadLink.hidden = false;
         pdfDownloadLink.hidden = false;
    } */