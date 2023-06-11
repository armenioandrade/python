value = input('Digite um valor: ')
print('Esse valor é numérico? {}. '
      'Esse valor é alfanumérico? {} '
      'Esse valor está em maiúsculo? {} '
      'Esse valor está em minúsculo? {} '
      'O tipo desse valor é: {}'
      .format(value.isnumeric(), value.isalnum(), value.isupper(), value.islower(), type(value)))
