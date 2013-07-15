/* 
 * veejay pyhton module is based on sendVIMS
 * 
 * sendVIMS - very simple client for VeeJay
 * 	     (C) 2002-2004 Niels Elburg <elburg@hio.hen.nl> 
 *
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <netdb.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <veejay/vims.h>
#include <veejay/vj-client.h>
#include <veejay/vjmem.h>
#include <veejay/vj-msg.h>

vj_client *my_client = NULL;

void vj_flush(int frames) {
  char status[100];
  bzero(status, 100);
  while (frames > 0) {
    if (vj_client_poll(my_client, V_STATUS)) {
      char sta_len[6];
      bzero(sta_len, 6);
      int nb = vj_client_read(my_client, V_STATUS, sta_len, 5);
      if (sta_len[0] == 'V') {
	int bytes = 0;
	sscanf(sta_len + 1, "%03d", &bytes);
	if (bytes > 0) {
	  bzero(status, 100);
	  int n = vj_client_read(my_client, V_STATUS, status, bytes);
	  if (n) {
	    if (0)
	      fprintf(stdout, "%s\n", status);
	    frames--;
	  }
	  if (n == -1) {
	    fprintf(stderr, "Error reading status from Veejay\n");
	    exit(0);
	  }
	}
      }
    }
  }
}

void conn_open() {
  veejay_set_debug_level(0);
  //printf("mem init\n");
  vj_mem_init();
  if (!my_client) {
    //printf("client alloc\n");
    my_client = vj_client_alloc(0, 0, 0);
    if (!my_client) {
      fprintf(stderr, "Memory allocation error\n");
    }
  }
  //printf("client connect\n");
  if (!vj_client_connect(my_client, "localhost", NULL, 3490)) {
    fprintf(stderr, "Unable to connect to %s:%d\n", "localhost", 3490);
  }
}

void command(char *cmd) {
  vj_client_send(my_client, V_CMD, cmd);
}

void end_flush() {
  vj_flush(1);
  vj_client_close(my_client);
  vj_client_free(my_client);
}
