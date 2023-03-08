import os
import logging
import nuconfig

log = logging.getLogger(__name__)
logging.root.setLevel("INFO")
log.debug("Set logging level to INFO while the config is being loaded")

# Ensure the template config file exists
if not os.path.isfile("config/template_config.toml"):
    log.fatal("config/template_config.toml does not exist!")
    exit(254)

# If the config file does not exist, clone the template and exit
if not os.path.isfile("config/config.toml"):
    log.debug("config/config.toml does not exist.")

    with open("config/template_config.toml", encoding="utf8") as template_cfg_file, \
            open("config/config.toml", "w", encoding="utf8") as user_cfg_file:
        # Copy the template file to the config file
        user_cfg_file.write(template_cfg_file.read())

    log.fatal("A config file has been created in config/config.toml."
                " Customize it, then restart greed!")
    exit(1)

# Compare the template config with the user-made one
with open("config/template_config.toml", encoding="utf8") as template_cfg_file, \
        open("config/config.toml", encoding="utf8") as user_cfg_file:
    template_cfg = nuconfig.NuConfig(template_cfg_file)
    user_cfg = nuconfig.NuConfig(user_cfg_file)
    if not template_cfg.cmplog(user_cfg):
        log.fatal("There were errors while parsing the config.toml file. Please fix them and restart greed!")
        exit(2)
    else:
        log.debug("Configuration parsed successfully!")