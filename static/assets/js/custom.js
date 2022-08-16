function fillParentId(commentId) {
    $('#parentComment').val(commentId);
    Scroll();
}
function Scroll(){
    //TODO: Fix Scrolling
    let to_scroll = document.getElementById('focusContextMessage');
    to_scroll.scrollIntoView({behavior: "smooth"});
}