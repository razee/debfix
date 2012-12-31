CustomButton = {

1: function () {
    var w = document.getElementById("content").contentWindow;  // window
    var t = (w.getSelection && w.getSelection());
    if (t != '') {
      // open selection in new window
      var str = 'http://translate.google.com/?text=' + t + '&hl=en&langpair=auto|en&tbb=1&ie=UTF-8';
      w.open(str);
    } else
      w.location.href = 'http://translate.google.com/translate?u=' + escape(w.location.href) + '&hl=en&langpair=auto|en&tbb=1&ie=UTF-8';
  },

}
