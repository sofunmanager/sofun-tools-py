
import subprocess

def initAutor(svn_url,svn_username,svn_password):
    svn_url=svn_url
    svn_username=svn_username
    svn_password=svn_password

#获取svn提交记录
def get_svn_log(url,username, password,limit):
    cmd = ['svn', 'log', '-l', str(limit)]
    cmd = ['svn', 'log', url, '-l', str(limit), '--username', username, '--password', password]  # 设置svn命令和参数
    result = subprocess.run(cmd, capture_output=True, text=True)
    log_output = result.stdout.strip()
    log_entries = log_output.split('\n\n')
    
    commit_logs = []
    for entry in log_entries:
        
        lines = entry.strip().split('\n')
        index=0
        message=""
        if(len(lines)==1):
            continue

        if(len(lines)>2):
            index=1
            message=lines[0]
        
        infos = lines[index+1].split(' | ')

        commit_logs.append({
            'revision': infos[0],
            'author': infos[1],
            'date': infos[2],
            'num': infos[3],
            'message': message
        })

    return commit_logs


# get_svn_log示例用法
# commit_logs = get_svn_log(svn_url, 5, svn_username, svn_password)
# 结果:[{'revision': 'r826', 'author': 'jys2', 'date': '2023-07-10 11:01:53 +0800 (周一, 10 7月 2023)', 'num': '1 line', 'message': ''},....]


#获取版本提交详情
def get_svn_log_detail(url, revision, username, password):
    cmd = ['svn', 'log', url, '-r', str(revision), '--username', username, '--password', password, '--verbose']  # 设置svn命令和参数
    result = subprocess.run(cmd, capture_output=True, text=True)  # 执行svn命令并捕获输出
    output = result.stdout  # 获取输出内容
    lines = output.splitlines()
    changed_paths = []
    for line in lines:
        if line.startswith('   '):
            action, file_path = line.strip().split(' ', 1)
            changed_paths.append({
                 "action":action,
                 "file_path":file_path,
            })
    return changed_paths

# get_svn_log_detail示例
# changed_paths = get_svn_log_detail(svn_url, "r810", svn_username, svn_password)
#[{'action': 'M', 'file_path': '/WebRoot/oa/duBan/lxjb/lx_detail.jsp'},.....]