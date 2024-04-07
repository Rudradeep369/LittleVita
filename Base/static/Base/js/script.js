console.log("Hello from script.js!");

// For the pop up message box

document.querySelector('.cancel-message').addEventListener('click', function () {
	var messageBox = document.querySelector('.message-box');
	messageBox.style.display = 'block'; // Show the message box
	messageBox.style.display = 'none';

});


setTimeout(function () {
	var messageBox = document.querySelector('.message-box');
	messageBox.style.display = 'block'; // Show the message box
	messageBox.style.display = 'none';
}, 3000);



document.addEventListener('DOMContentLoaded', (event) => {
    let lastScrollTop = 0;
    const navbar = document.querySelector('.navbar');

	// console.log("scrolling");
    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        
        if (scrollTop < lastScrollTop) {
            navbar.classList.remove('hide');
        } else {
            navbar.classList.add('hide');
        }
        lastScrollTop = scrollTop;
    });
});






function pageStart(){
	// let load= document.body.querySelector(".loaderPageContainer");
    // load.style.display='none';
	const skeletonLoader = document.querySelector('.skeleton-loader');
    skeletonLoader.style.display = 'none';

}