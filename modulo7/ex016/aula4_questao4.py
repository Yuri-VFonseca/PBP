'''Vamos fazer o jogo da forca! Antes de programar: 

Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.

Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.
Escreva um programa em Python para executar o jogo, de acordo com as definições:

Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;

Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;

No início exiba o número de letras na palavra como underscores;

Permita que o jogador insira letras para adivinhar a palavra;

Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;

Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;

Limite o número de tentativas para 6 (as partes do enforcado).

gabarito_enforcado.txt

  |---|

      |

      |

      |

=========


  |---|

  O   |

      |

      |

=========


  |---|

  O   |

  |   |

      |

=========


  |---|

  O   |

 /|   |

      |

=========

 

  |---|

  O   |

 /|\  |

      |

=========

 

  |---|

  O   |

 /|\  |

 /    |

=========

 

  |---|

  O   |

 /|\  |

 / \  |

========='''