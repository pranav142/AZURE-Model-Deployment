const fileDropArea = document.querySelector(".dropzone");
const dropText = document.querySelector(".file-drop-text");
const invalidFileWarning = document.querySelector(".invalid-warning");
let imagePresent = false;

const dragArea = document.querySelector('.drag-area');
const dragText = document.querySelector('.header');
let BrowseButton = document.querySelector('.browseButton');

let uploadInput = document.getElementById('submit');
let fileInput = document.getElementById('file');

let file;

BrowseButton.onclick = () => {
    fileInput.click();
};

function uploadImage(){
    try{
        uploadInput.click();
    } catch(error){
        console.log('An error occurred: ' + error.message);
    }
}

fileInput.addEventListener('change', function () {
    file = this.files[0];
    dragArea.classList.add('active');
    displayFile();
})

function displayFile() {
    let fileType = file.type;
    let validExtensions = ['image/jpeg', 'image/jpg'];

    if(validExtensions.includes(fileType)){
        let fileReader = new FileReader();

        fileReader.onload = () => {
            let fileUrl = fileReader.result;

            let img_tag = `<img src="${fileUrl}" alt="">`;
            dragArea.innerHTML = img_tag;
        };
        fileReader.readAsDataURL(file)
    } else {
        alert('This File is Not an Accepeted Type. Please Submit a JPG, or JPEG.');
        dragArea.classList.remove('active');
    }
}
