<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>

<!-- jQuery Modal -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.css"/>
<script type="text/javascript">
$(".points").on("click", function(e){
    e.preventDefault();
    console.log(e.target);
    $("#send_form").attr('action', 'test'+ e.target.id +'.php');
    $('#id_p').text(e.target.id);
    $('#cluster_no_p').text($(this).attr('cluster_no'));
    
    $("#ex1").modal();
    alert('test');
});
</script>