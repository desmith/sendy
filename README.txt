Basic Usage
===========

Introduction
------------

The sendyrsspub.py command is the only command you need to use in order to use
this software. There are, however, a few supporting files that are required
in order for everything to work:

    settings.py -> the default settings, which can be overridden on the
                   command line.
    templates   -> the directory which contains the text and html templates
                   used for rendering newsletters.
    feed_log.db -> a database of feed items that have been processed. This
                   is required to prevent duplicate messages from being sent.

These files are explained in more detail below.

Getting Help
------------

Most commands are documented via help on the command line. For example, to
see the top level commands, you can type the following:

    python sendyrsspub.py -h

To see additional help about a specific command (i.e. in this case, the
test_feed command), you can type the following:

    python sendyrsspub.py test_feed -h

Now onto getting the software setup...

1. Configure Default Settings
-----------------------------

Edit the file settings.py and change the settings to match your current
environment. Generally, you can leave the default database name (feed_log.db)
as-is - there are very few cases when you will need to change this. For
testing, you can also leave the default template names as-is.

2. Test Reading the Feed URL
----------------------------

Enter the following command on the command line:

    python sendyrsspub.py test_feed

This will read the RSS feed and output the contents as a Python data structure.
You will need this information for creating your newsletter templates. If you
like, you can output this data to a text file by as follows:

    python sendyrsspub.py test_feed > feed_data.txt

3. Test the Newsletter Templates
--------------------------------

You can test the currently configured newsletter templates by typing the
following on the command line:

    python sendyrsspub.py test_template

This command will read the feed and use the data from that feed to render the
templates configured in settings.py to stdout. To render a specific template,
other than those configured in settings.py, you can type the following instead:

   python sendyrsspub.py test_template --template template_name.html

You can create your own newsletter templates, using the example ones as
a basic reference. Templates are rendered using the Jinja 2 templating engine.
For more info on how this templating engine works, you can visit the
documentation here:

    http://jinja.pocoo.org/docs/dev/

The data supplied to the templates comes from the data from the feed, as was
tested in step 2. Once you create your own custom templates, you can configure
those templates to be used by default in the settings.py file.

4. Send the Newsletter
----------------------

Once the template rendering is working as expected, you can send a newsletter
as follows:

    python sendyrsspub.py send_newsletter

You can run this command via cron at any interval you like to have a
newsletter sent automatically. If there are no new items in the feed, no
newsletter will be sent.

5. Maintaining the Database
---------------------------

The database can be cleaned and/or pruned using the db_clean and db_prune
commands. See the command-line documentation for more details.
