// 表单验证
$('input[name=uname]').blur(function(){
         val=this.value;
        if(val.length<6){
            $(this).data({'s':0});
            $(this).next().show();
        }else{
            $(this).data({'s':1});
            $(this).next().hide();
        }
});
$('input[name=upwd]').blur(function(){
    val=this.value;
    if(val.length<6){
        $(this).data({'s':0});
        $(this).next().show();
        }else{
            $(this).data({'s':1});
            $(this).next().hide();
        }
});

$('input[name=cpwd]').blur(function(){
    val1=$('input[name=password]').val();
    val2=this.value;
    if(val1!=val2){
            $(this).data({'s':0});
            $(this).next().show();
        }else{
            $(this).data({'s':1});
            $(this).next().hide();
        }
});
$('input[name=imgCode]').blur(function(){
    val=this.value;
    if(val.length!=4){
        $(this).data({'s':0});
        $(this).next().show();
        }else{
            $(this).data({'s':1});
            $(this).next().hide();
        }
});
$('form').submit(function(){
    $('.text').blur();
    tot=0;
    $('.text').each(function(){
        tot+=$(this).data('s');
    });
    if(tot!=3){
    return false;
    }
});

