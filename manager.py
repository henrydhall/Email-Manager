import ezgmail
import os

def searchBySender(senderToSearch):
    print('Searching for emails...')
    sendersToSearch = ['Facebook','Amazon.com','Amazon Prime','Robinhood Snacks']
    searchedEmails = ezgmail.search(maxResults=2000, query=f'from:{senderToSearch}' )
    return searchedEmails

def deleteEmails(emailsToDelete):
    print(f'Deleting {len(emailsToDelete)} emails...')
    for email in emailsToDelete:
        email.trash()

if __name__ == '__main__':
    ezgmail.init()
    senderToDelete = 'Netflix'
    searchedEmails = searchBySender(senderToDelete)
    while(len(searchedEmails)) > 0:
        deleteEmails(searchedEmails)
        searchedEmails = searchBySender(senderToDelete)