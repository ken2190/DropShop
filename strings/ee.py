# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Part of the translation by https://github.com/DarrenWestwood

# Currency symbol
currency_symbol = "€"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} saadaval"

# Copies of a product in cart
in_cart_format_string = "{quantity} ostukorvis"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Tellimus #{id}"

# Order info string, shown to the admins
order_format_string = "by {user}\n" \
                      "Created on {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "TOTAL: <b>{value}</b>\n" \
                      "\n" \
                      "Customer notes: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Tellimus {status_text}</b>\n" \
                           "{items}\n" \
                           "Kokku: <b>{value}</b>\n" \
                           "\n" \
                           "Märkused: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Laen tehinguid...\n" \
                       "Oodake mõni hetk.</i>"

# Transactions page
transactions_page = "Lehekülg <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "Loodi 📄 .csv fail, mis sisaldab kõiki bot'i andmebaasis salvestatud tehinguid.\n" \
              "Seda faili saab avada teiste programmidega, näiteks LibreOffice Calciga, et seda töödelda." \
              " andmeid."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Tere!\n" \
                           "Tere tulemast Apteek+-i\n" \
                           "See on 🅱️ <b>Beta</b> versioon.\n" 


# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "Mida soovid teha?\n" \
                              "💰 Teil on <b>{credit}</b> isiklikul kontol.\n" \
                              "\n" \
                              "<i>Press a key on the bottom keyboard to select an operation.\n" \
                              "If the keyboard has not opened, you can open it by pressing the button with four small" \
                              " squares in the message bar.</i>"

# Conversation: like above, but for administrators
conversation_open_admin_menu = "Sa oled selle poe 💼 <b>Manager</b>! \n" \
                               "Mida soovid teha?\n" \
                               "\n" \
                               "<i>Valige nupp teksti all.\n" \
                               "If the keyboard has not opened, you can open it by pressing the button with four small" \
                               " squares in the message bar.</i>"

# Conversation: select a payment method
conversation_payment_method = "Kuidas soovite kontole raha lisada?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Millist toodet soovite muuta"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Millist toodet soovid kustutada?"

# Conversation: select a user to edit
conversation_admin_select_user = "Vali kasutaja mida muuta."

# Conversation: click below to pay for the purchase
conversation_cart_actions = "<i>Lisa tooted ostukorvi, kerides ülespoole ja vajutades allolevat nuppu Lisa\n"\
                            " tooted, mida soovite ostukorvi lisada. Kui olete lõpetanud, minge tagasi selle sõnumi juurde ja\n" \
                            " vajutage allpool olevat nuppu Valmis.</i>"

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Ostukäru sisaldab järgenvaid tooteid:\n" \
                            "{product_list}" \
                            "Kokku: <b>{total_cost}</b>\n" \
                            "\n" \
                            "<i>Kui soovite jätkata, vajutage selle teate all olevale nupule Valmis..\n" \
                            "Tühistamiseks vajutage nuppu Tühista.</i>"

# Live orders mode: start
conversation_live_orders_start = "You are in <b>Live Orders</b> mode\n" \
                                 "All new orders placed by customers will appear in real time in this chat, and you" \
                                 " will be able to mark them as ✅ Completed" \
                                 " or ✴️ Refund the credit to the customer."

# Live orders mode: stop receiving messages
conversation_live_orders_stop = "<i>Press the Stop button below this message to stop the" \
                                " feed.</i>"

# Conversation: help menu has been opened
conversation_open_help_menu = "Millega abi vajate?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Are you sure you want to promote this user to 💼 Manager?\n" \
                                       "It is an irreversible action!"

# Conversation: language select menu header
conversation_language_select = "Valige keel:"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Vahetate 👤 kliendi reziimi.\n" \
                                   "If you want to go back to the 💼 Manager menu, restart the conversation with /start."

# Notification: the conversation has expired
conversation_expired = "🕐  Ma ei ole juba mõnda aega ühtegi sõnumit saanud, nii et ma sulgesin vestluse, et säästa" \
                       " ressursse.\n" \
                       "Kui soovite käivitada uut vestlust, saatke uus käsk /start."

# User menu: order
menu_order = "🛒 Telli tooteid"

# User menu: order status
menu_order_status = "🛍 Minu tellimused"

# User menu: add credit
menu_add_credit = "💵 Lisa raha"

# User menu: bot info
menu_bot_info = "ℹ️ Arvustused"

# User menu: cash
menu_cash = "💵 Sularahas"

# User menu: credit card
menu_credit_card = "💳 Pangakaardiga"

# Admin menu: products
menu_products = "📝️ Tooted"

# Admin menu: orders
menu_orders = "📦 Tellimused"

# Menu: transactions
menu_transactions = "💳 Tehingute Nimekiri"

# Menu: edit credit
menu_edit_credit = "💰 Loo tehing"

# Admin menu: go to user mode
menu_user_mode = "👤 Switch to customer mode"

# Admin menu: add product
menu_add_product = "✨ Uus toode"

# Admin menu: delete product
menu_delete_product = "❌ Kustuta toode"

# Menu: cancel
menu_cancel = "🔙 Tühista"

# Menu: skip
menu_skip = "⏭ Jäta vahele"

# Menu: done
menu_done = "✅️ Valmis"

# Menu: pay invoice
menu_pay = "💳 Maksa"

# Menu: complete
menu_complete = "✅ Tehtud"

# Menu: refund
menu_refund = "✴️ Refund"

# Menu: stop
menu_stop = "🛑 Peata"

# Menu: add to cart
menu_add_to_cart = "➕ Lisa"

# Menu: remove from cart
menu_remove_from_cart = "➖ Eemalda"

# Menu: help menu
menu_help = "❓ Abi"

# Menu: guide
menu_guide = "📖 Õpetus"

# Menu: next page
menu_next = "▶️ Järgmine"

# Menu: previous page
menu_previous = "◀️ Eelmine"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Võta ühendust operaatoriga"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Edit Managers"

# Menu: language
menu_language = "🇪🇪 Keel"

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "Töötlemisel"

# Text: completed order
text_completed = "Valmis"

# Text: refunded order
text_refunded = "Tagastatud"

# Add product: name?
ask_product_name = "Mis peaks olema toote nimi?"

# Add product: description?
ask_product_description = "Toote kirjeldus?"

# Add product: price?
ask_product_price = "Toote hind?\n" \
                    "Sisesta <code>X</code> Kui toode pole veel müügis."

# Add product: image?
ask_product_image = "🖼 Toote pilt??\n" \
                    "\n" \
                    "<i>Send the photo, or Skip this phase and don't add any image.</i>"

# Order product: notes?
ask_order_notes = "Sisesta asukoht/linnaosa kuhu soovid tellimuse saada \n" \
                  "💼 Seda näeb ainult poe operaator.\n"


# Refund product: reason?
ask_refund_reason = " Lisa tagastuse põhjus.\n" \
                    "👤  It will be visible to the customer."

# Edit credit: notes?
ask_transaction_notes = " Lisa tehingule märge.\n" \
                        "👤 Klient näeb peale arveldamist / debiting" \
                        " ja 💼 Admin tehingute logis."

# Edit credit: amount?
ask_credit = "Kuidas soovite muuta krediiti?\n" \
             "\n" \
             "<i>Saada sõnum kogusega.\n" \
             "Use the sign </i><code>+</code><i> to add credit to the customer's account," \
             " and the sign </i><code>-</code><i> to deduce it.</i>"

# Header for the edit admin message
admin_properties = "<b>{name} õigused:</b>"

# Edit admin: can edit products?
prop_edit_products = "Muuda tooteid"

# Edit admin: can receive orders?
prop_receive_orders = "Tellimuste vastuvõtmine"

# Edit admin: can create transactions?
prop_create_transactions = "tehingute haldamine"

# Edit admin: show on help message?
prop_display_on_help = "Näita kliendile"

# Thread has started downloading an image and might be unresponsive
downloading_image = "I'm downloading your photo!\n" \
                    "It might take a while... Please be patient!\n" \
                    "I won't be able to answer you while I'm downloading."

# Edit product: current value
edit_current_value = "Hetkeväärtus on:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Press the Skip button below this message to keep the same value.</i>"

# Payment: cash payment info
payment_cash = "Sularahas maksta ei saa hetkel.\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "Kui palju raha soovite lisada oma kontole?\n" \
                    "\n" \
                    "<i>Valige kogus valikutest, või sisestage käsitsi</i>"

# Payment: add funds invoice title
payment_invoice_title = "Raha lisamine"

# Payment: add funds invoice description
payment_invoice_description = "Selle koguse maksmine lisab {amount} su isiklikule kontole."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Lae uuesti"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Tehingutasu"

# Notification: order has been placed
notification_order_placed = "A new order was placed:\n" \
                            "\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Teie tellimus on valmis\n" \
                               "\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Teie tellimus on tühistatud ja raha kontole tagastatud!\n" \
                              "\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  Uus tehing tehtud teie rahakotiga:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Tagastuse põhjus:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = "https://t.me/apteekPlus_reviews"

# Help: guide
help_msg = "Abi jaoks kirjutage poe omanikule" \
        "t.me/APTEEKPLUS\n" 

# Help: contact shopkeeper
contact_shopkeeper = "Poe operaator:\n" \
                     "t.me/APTEEKPLUS\n" \
                     "<i>Vajutage nimele kontakteerumiseks.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ Toode on edukalt lisatud/muudetud!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ Toode on edukalt kustutatud!"

# Success: order has been created
success_order_created = "✅ Tellimus on edukalt esitatud\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ Tellimus #{order_id} on nüüd VALMIS."

# Success: order was refunded successfully
success_order_refunded = "✴️ Tellimus #{order_id} tühistati ja raha tagastati teie kontole."

# Success: transaction was created successfully
success_transaction_created = "✅ Tehing on edukalt loodud!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ See bot töötab ainult privaatsetes vestlustes.(SECRET CHAT)"

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ Vestlus botiga katkes.\n" \
                           "Kasutage /start uuesti alustamiseks ."

# Error: a message was sent in a chat, but the worker for that chat is not ready.
error_worker_not_ready = "🕒 Vestlus botiga on praegu algamas.\n" \
                         "Palun, oodake mõni hetk, enne kui saadate veel käske!"

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ Maksimaalne summa, mida saab ühe tehinguga lisada, on {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ Minimaalne summa, mida saab ühe tehinguga lisada, on {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ See arve on aegunud ja tühistatud. Kui soovite siiski raha lisada, kasutage nuppu 'Lisa'\n"\
                        " rahaliste vahendite lisamise menüüvalikut."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Sama nimega toode on juba olemas."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ Teil ei ole tellimuse tegemiseks piisavalt krediiti."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  Tellimus on juba töödeldud."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  Te ei ole veel ühtegi tellimust teinud, seega ei ole midagi kuvada."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  Sellist kasutajat pole."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh ei! Viga <b>error</b> segas seda vestlust\n" \
                               "Veast teatati boti omanikule, et ta saaks selle parandada..\n" \
                               "Vestluse taaskäivitamiseks saatke uuesti käsk /start."
menu_category = "Category"
menu_region = "Linnaosa"
menu_packagesize = "How much do you need"
ask_product_category = "What category is said product?"
ask_product_region = "Where is it located"
ask_product_packagesize = "How big drop is it"
conversation_select_category = "Select a category"
error_category_does_not_exist = "⚠️  The selected category does not exist."
error_region_does_not_exist = "⚠️  The selected region does not exist."
error_no_products = "⚠️  There are no products currently in stock"
error_no_products_in_category = "⚠️  There are no products in this category"
error_size_does_not_exist = "⚠️  The selected size does not exist."
error_insufficient_funds = "⚠️  You do not have enough credit to place the order."
menu_yes    = "✅Yes"
menu_no = "⚠️No"
menu_confirm = "✅Confirm"
menu_successful_purchase = "✅Successful purchase of {category}\n in Region📍: {region}\n {packagesize} grams\nfor {price}€.\n Remaining balance: {credit}€"