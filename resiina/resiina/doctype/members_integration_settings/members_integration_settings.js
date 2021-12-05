// Copyright (c) 2021, Mitja Karhusaari <mitja.karhusaari@helsinki.fi> and contributors
// For license information, please see license.txt

frappe.ui.form.on('Members Integration Settings', {
  refresh: (frm) => {
    frm.add_custom_button('Synchronize', async () => {
      if (frm.is_dirty()) {
        await frm.save();
      }

      const { message } = await frappe.call('resiina.integration.sync_members');

      frappe.msgprint({
        title: __('Synchronization Raport'),
        indicator: 'blue',
        message: `Synchronized ${message.failed + message.successful} members, with ${message.failed} failures.`,
      })
    });

    frm.add_custom_button('Test Connection', async () => {
      if (frm.is_dirty()) {
        await frm.save();
      }

      const { message } = await frappe.call('resiina.integration.test_members_connection');

      if (message.success) {
        frappe.msgprint({
          title: __('Database Connection Test'),
          indicator: 'green',
          message: __('Database connection was established successfully.'),
        });
      } else {
        frappe.msgprint({
          title: __('Database Connection Test'),
          indicator: 'red',
          message: __('Database connection could not be established.'),
        })
      }
    });
  },
  // refresh: function(frm) {

  // }
});
