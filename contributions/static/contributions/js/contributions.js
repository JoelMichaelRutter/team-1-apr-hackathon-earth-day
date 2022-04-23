
const submitButtons = document.querySelectorAll('[type=submit]');
const commentInputs = document.querySelectorAll('textarea');


submitButtons.forEach(button => button.addEventListener('click', (event) => {
    event.preventDefault;
    console.log(event.target.id)
}))

const countChars = (elemID, chars) => {

    const maxLength = 280;
    let strLength = chars.length;
    let charRemain = (maxLength - strLength);
    let label = document.querySelector("label[for='" + elemID + "']");
    let currentLabelText = label.innerHTML
    
    if(charRemain < 0){
        label.innerHTML = '<span style="color: red;">You have exceeded the limit of '+maxLength+' characters</span>';
    }
    else {
        label.innerHTML = charRemain+' characters remaining';
    }
}

commentInputs.forEach(input => input.addEventListener('keyup', (event) => {
    elemID = event.target.id;
    chars = event.target.value;
    countChars(elemID, chars)
}))