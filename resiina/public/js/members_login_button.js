const memberLoginButton = $('<button>')
  .addClass('btn btn-sm btn-default btn-block btn-members-login')
  .text(__('Login with TKO-äly Member Account'))
  .click(() => {
    frappe
      .call('resiina.integration.get_user_service_url')
      .then(({ message }) => {
        window.location = message;
      });
  });

$('.form-login').append($('<h6>').text('— Or —'));
$('.form-login').append(memberLoginButton);
