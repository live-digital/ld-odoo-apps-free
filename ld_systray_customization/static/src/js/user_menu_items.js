/** @odoo-module **/
import { UserMenu } from "@web/webclient/user_menu/user_menu";
import { patch } from "@web/core/utils/patch";
import { registry } from "@web/core/registry";
import { MessagingMenuContainer } from '@mail/components/messaging_menu_container/messaging_menu_container';

const systrayRegistry = registry.category('systray');
patch(MessagingMenuContainer.prototype, "ld_systray_customization.MessagingMenuContainer", {

    setup() {
        this._super.apply(this, arguments);
        systrayRegistry.remove('mail.MessagingMenuContainer');
        systrayRegistry.remove('mail.ActivityMenu');
    },

});

const userMenuRegistry = registry.category("user_menuitems");

patch(UserMenu.prototype, "ld_systray_customization.UserMenu", {

    setup() {
        this._super.apply(this, arguments);
        const removeMenus = ["documentation", "support", "shortcuts", "odoo_account"];
        removeMenus.forEach(function valsIter(value, index, array) {
            userMenuRegistry.remove(value);
        });
    },

});