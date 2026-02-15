#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <getopt.h>

void print_help(char *prog_name) {
    printf("Usage: %s [option] <path/filename>\n", prog_name);
    printf("Options:\n");
    printf("  -h, --help     Show this help message\n");
    printf("  -cpp           Generate C++ template\n");
    printf("  -py            Generate Python template\n");
}

void write_cpp(FILE *fp) {
    fprintf(fp, "#include <bits/stdc++.h>\n\n");
    fprintf(fp, "using namespace std;\n\n");
    fprintf(fp, "void solve() {\n\t\n}\n\n");
    fprintf(fp, "int main() {\n");
    fprintf(fp, "\tios::sync_with_stdio(false);\n");
    fprintf(fp, "\tcin.tie(nullptr);\n");
    fprintf(fp, "\tint t = 1;\n");
    fprintf(fp, "\t// cin >> t;\n");
    fprintf(fp, "\twhile (t--) {\n");
    fprintf(fp, "\t\tsolve();\n");
    fprintf(fp, "\t}\n");
    fprintf(fp, "\treturn 0;\n}\n");
}

void write_py(FILE *fp) {
    fprintf(fp, "import sys, os, math, biect, heapq, collections, itertools, functools, re\n");
    fprintf(fp, "input = sys.stdin.readline\n\n");
    fprintf(fp, "############ ---- Input Functions ---- ############\n");
    fprintf(fp, "def inp():\n\treturn (int(input()))\n\n");
    fprintf(fp, "def inlt():\n\treturn (list(map(int,input().split())))\n\n");
    fprintf(fp, "def insr():\n\ts = input()\n\treturn (list(s[:len(s) - 1]))\n\n");
    fprintf(fp, "def invr():\n\treturn (map(int,input().split()))\n");
}

int main(int argc, char *argv[]) {
    int mode = 0; // 1 for CPP, 2 for PY
    
    // Define long options for -cpp and -py
    static struct option long_options[] = {
        {"help", no_argument, 0, 'h'},
        {"cpp",  no_argument, 0, 'c'},
        {"py",   no_argument, 0, 'p'},
        {0, 0, 0, 0}
    };

    int opt;
    while ((opt = getopt_long_only(argc, argv, "h", long_options, NULL)) != -1) {
        switch (opt) {
            case 'h': print_help(argv[0]); return 0;
            case 'c': mode = 1; break;
            case 'p': mode = 2; break;
            default: return 1;
        }
    }

    if (optind >= argc) {
        printf("Error: Please provide a filename/path.\n");
        return 1;
    }

    char *filename = argv[optind];
    char full_name[512];
    
    if (mode == 1) snprintf(full_name, sizeof(full_name), "%s.cpp", filename);
    else if (mode == 2) snprintf(full_name, sizeof(full_name), "%s.py", filename);
    else {
        printf("Error: Specify -cpp or -py\n");
        return 1;
    }

    FILE *fp = fopen(full_name, "w");
    if (!fp) {
        perror("File Error");
        return 1;
    }

    if (mode == 1) write_cpp(fp);
    else write_py(fp);

    fclose(fp);
    printf("Created template at: %s\n", full_name);
    return 0;
}
