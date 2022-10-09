from searching.searching import Searching

try:
    with Searching() as bot:
        bot.landing_page()
        bot.what_text_box(input("Developer position? "))
        bot.where_text_box("Canton, GA")
        bot.find_jobs_btn()
        bot.apply_filtration(input("Developer Skill? (Case-sensitive. Must choose one.) "))
        bot.refresh() # Allow the bot to properly retrieve the data
        bot.report_results(input("How many result pages do you want to be returned? "))
        bot.quit()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from the command line \n'
            'Please add the Selenium Driver to your PATH \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise



