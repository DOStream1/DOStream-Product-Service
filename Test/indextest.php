<?php
use PHPUnit\Framework\TestCase;

class LoginTest extends TestCase
{
    public function testLoginPage()
    {
        $_SESSION['logged_in'] = false;

        ob_start();
        include 'login.php';
        $output = ob_get_clean();

        $this->assertStringContainsString('<title>4S Consult | Login</title>', $output);
        $this->assertStringContainsString('<form id="LoginFrm" method="post" action="<?=base_url?>login.php">', $output);
        $this->assertStringContainsString('<label for="txtEmailID" class="form-label">Enter Email ID</label>', $output);
        $this->assertStringContainsString('<input type="email" class="form-control" id="email" name="emailid" placeholder="Enter Email ID">', $output);
        $this->assertStringContainsString('<label for="txtOTP" class="form-label">Enter Verification Code</label>', $output);
        $this->assertStringContainsString('<input type="text" class="form-control" id="otp" name="otp" placeholder="Enter Verification Code" maxlength="6">', $output);
        $this->assertStringContainsString('<a href="javascript:void(0)" style="display:none" class="btn-fs-primary lgn_btn">Login </a>', $output);
        $this->assertStringContainsString('<a href="<?=base_url . \'register.php\'?>">Register Now</a>', $output);
    }
}
