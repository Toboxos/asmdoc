var coll = document.getElementsByClassName('collapsible');

for( var i = 0; i < coll.length; ++i ) {
    coll[i].addEventListener('click', function() {
        this.classList.toggle("active");

        var content = this.nextElementSibling;
        content.classList.toggle('active');
        if( content.style.maxHeight ) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}