def talk_phrase(phrase):
      def say(words):
         print(words)
      words=phrase.split(' ')
      for words in words:
             say(words)

talk_phrase('iam going to get milk and never coming back')