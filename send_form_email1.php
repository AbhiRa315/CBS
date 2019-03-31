<?php
define('EMAIL','abhishek.rai315@gmail.com');
define('PASS','1541998abhishek');
$result="";
if (isset($_POST['txtEmailAddress'])) {
 require 'PHPMailerAutoload.php';
  $mail = new PHPMailer;
  //$mail->SMTPDebug = 4;                               // Enable verbose debug output

  $mail->isSMTP();
   $mail->Host='smtp.gmail.com';
   $mail->Port = 587;                                    // TCP port to connect to
   $mail->SMTPAuth = true;                               // Enable SMTP authentication
   $mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
   $mail->Username = 'abhishek.rai315@gmail.com';                 // SMTP username
   $mail->Password = '1541998abhishek';                           // SMTP password

   $mail->setFrom($_POST['txtEmailAddress'],$_POST['txtFirstName']);
   $mail->addAddress('abhishek.rai315@gmail.com',"myname");     // Add a recipient
  // $mail->addAddress('mark11.kale@gmail.com');
   $mail->addReplyTo($_POST['txtEmailAddress'],$_POST['txtFirstName']);

   $mail->isHTML(true);                                  // Set email format to HTML
   $mail->Subject = ' subject:'.$_POST['subject'];
   $mail->Body    = '<h1 align=center>First Name:'.$_POST['txtFirstName'].'Surname:'.$_POST['txtLastName'].'<br> Email:'.$_POST['txtEmailAddress'].'<br> Company:'. $_POST['txtCompany'].'<br> Message:'. $_POST['txtMessage'].'<h1>';

   if(!$mail->send()) {
       $result= "Message could not be sent.";
       echo 'Mailer Error: ' . $mail->ErrorInfo;
   } else {
    $result= "Message has been sent".$_POST['txtFirstName']."Thank YOU";

   }

echo <<<_END
<meta http-equiv='refresh' content='0;url=contact.html?msg=$result'>
_END;


}
 ?>
