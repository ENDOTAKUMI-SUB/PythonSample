def input_scores(name):
    print('{}さんの試験結果を入力してください。'.format(name))
    network = int(input('ネットワークの得点?'))
    log_write('network',network) 
    databese = int(input('データベースの得点?'))
    log_write('databese',databese)
    security = int(input('セキュリティの得点?'))
    log_write('security',security)
    scores =[network,databese,security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    log_write('scores',scores)
    return avg

def output_result(name, avg):
    print('{}さんの平均点は{}です。'.format(name,avg))

def log_write(name, value):
    # print('{}::{}'.format(name,value))
    pass

asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')

asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

output_result('浅木',asagi_avg)
output_result('松田',matsuda_avg)